import contextlib
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'skills/feature-forge/scripts/forge_support.py'
spec = importlib.util.spec_from_file_location('evidence_support', SCRIPT)
support = importlib.util.module_from_spec(spec)
spec.loader.exec_module(support)


class EvidenceTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name) / 'repo'
        self.repo.mkdir()
        self.git('init', '-q')
        self.git('config', 'user.name', 'Test')
        self.git('config', 'user.email', 'test@example.invalid')
        (self.repo / 'tracked').write_text('original')
        (self.repo / '.gitignore').write_text('secret.env\n')
        self.git('add', '.')
        self.git('commit', '-qm', 'Fixture')

    def git(self, *args):
        return subprocess.run(['git', '-C', str(self.repo), *args], check=True,
                              capture_output=True, text=True).stdout.strip()

    def run_check(self, name, code='print("proof")', context=None):
        evidence = self.repo / name
        with contextlib.redirect_stdout(io.StringIO()):
            status = support.verify(self.repo, evidence,
                                    [sys.executable, '-c', code], context)
        return status, json.loads((evidence / 'result.json').read_text()), evidence

    def test_dirty_untracked_deleted_mode_and_symlink_are_identified(self):
        (self.repo / 'tracked').write_text('dirty')
        new = self.repo / 'new file'
        new.write_text('new')
        new.chmod(0o755)
        (self.repo / '.gitignore').unlink()
        (self.repo / 'link').symlink_to('tracked')
        status, record, _ = self.run_check('evidence')
        files = {f['path']: f for f in record['before']['files']}
        self.assertEqual(status, 0)
        self.assertEqual(record['before']['revision'], self.git('rev-parse', 'HEAD'))
        self.assertEqual(files['.gitignore']['kind'], 'missing')
        self.assertEqual(files['new file']['mode'], '0o755')
        self.assertEqual(files['link']['kind'], 'symlink')
        self.assertIn('sha256', files['tracked'])
        self.assertFalse(record['changed_during_run'])
        self.assertEqual(record['before']['digest'], record['after']['digest'])
        prior = record['before']['digest']
        # Keep previous runs outside the scope of the next observation.
        self.git('config', 'core.excludesFile', str(self.repo.parent / 'ignores'))
        (self.repo.parent / 'ignores').write_text('evidence*\n')
        (self.repo / 'tracked').write_text('different dirty contents')
        _, changed, _ = self.run_check('evidence-next')
        self.assertNotEqual(prior, changed['before']['digest'])

    def test_command_mutation_and_setup_change_are_visible(self):
        setup = self.repo.parent / 'setup.json'
        setup.write_text(json.dumps({'runtime': 'example', 'external': 'test service, unpinned'}))
        code = ('from pathlib import Path; Path("tracked").write_text("changed"); '
                'Path(' + repr(str(setup)) + ').write_text(\'{"runtime":"other"}\')')
        status, record, evidence = self.run_check('evidence', code, setup)
        self.assertEqual(status, 0)
        self.assertTrue(record['changed_during_run'])
        self.assertNotEqual(record['before']['digest'], record['after']['digest'])
        self.assertEqual(record['setup_before']['runtime'], 'example')
        self.assertEqual(record['setup_after']['runtime'], 'other')
        original = (evidence / 'result.json').read_bytes()
        with self.assertRaises(ValueError):
            support.verify(self.repo, evidence, [sys.executable, '-c', 'pass'])
        self.assertEqual((evidence / 'result.json').read_bytes(), original)

    def test_ignored_secret_values_and_environment_are_not_collected(self):
        (self.repo / 'secret.env').write_text('DO_NOT_CAPTURE=secret-value')
        _, record, _ = self.run_check('evidence')
        self.assertNotIn('secret.env', [f['path'] for f in record['before']['files']])
        self.assertNotIn('secret-value', json.dumps(record))
        self.assertIn('ignored', record['before']['scope'])
        self.assertIn('external', record['limits'])

    def test_non_git_and_missing_executable_report_limits_and_failure(self):
        plain = self.repo.parent / 'plain'
        plain.mkdir()
        (plain / 'file').write_text('data')
        evidence = plain / 'evidence'
        with contextlib.redirect_stdout(io.StringIO()):
            status = support.verify(plain, evidence, [str(plain / 'absent-command')])
        record = json.loads((evidence / 'result.json').read_text())
        self.assertNotEqual(status, 0)
        self.assertIsNone(record['before']['revision'])
        self.assertIn('launch_error', record)
        self.assertEqual([f['path'] for f in record['before']['files']], ['file'])

    def test_capture_failure_keeps_command_status_and_original_output(self):
        setup = self.repo.parent / 'setup.json'
        setup.write_text('{}')
        status, record, evidence = self.run_check('evidence',
            'from pathlib import Path; print("real proof"); '
            'Path(' + repr(str(setup)) + ').write_text("invalid json")', setup)
        self.assertNotEqual(status, 0)
        self.assertEqual(record['exit_code'], 0)
        self.assertIn('capture_error', record)
        self.assertIsNone(record['after'])
        self.assertTrue(record['changed_during_run'])
        self.assertIn('real proof', (evidence / 'output.log').read_text())

    def test_symlinked_parent_does_not_read_tracked_descendants_outside_repo(self):
        directory = self.repo / 'dir'
        directory.mkdir()
        (directory / 'tracked').write_text('original')
        self.git('add', 'dir')
        self.git('commit', '-qm', 'Add directory')
        directory.rename(self.repo.parent / 'old-directory')
        outside = self.repo.parent / 'outside'
        outside.mkdir()
        (outside / 'tracked').write_text('external contents')
        directory.symlink_to(outside, target_is_directory=True)
        _, record, _ = self.run_check('evidence')
        files = {f['path']: f for f in record['before']['files']}
        self.assertEqual(files['dir']['kind'], 'symlink')
        self.assertEqual(files['dir/tracked']['kind'], 'unfingerprinted-symlink-parent')
        self.assertEqual(files['dir/tracked']['boundary'], 'dir')
        self.assertNotIn('sha256', files['dir/tracked'])

    def test_directory_replaced_by_file_records_dirty_state_and_runs_command(self):
        directory = self.repo / 'dir'
        directory.mkdir()
        (directory / 'tracked').write_text('original')
        self.git('add', 'dir')
        self.git('commit', '-qm', 'Add directory')
        directory.rename(self.repo.parent / 'old-directory')
        directory.write_text('replacement file')
        status, record, evidence = self.run_check('evidence')
        files = {f['path']: f for f in record['before']['files']}
        self.assertEqual(status, 0)
        self.assertEqual(files['dir']['kind'], 'file')
        self.assertEqual(files['dir/tracked']['kind'], 'missing')
        self.assertIn('proof', (evidence / 'output.log').read_text())
