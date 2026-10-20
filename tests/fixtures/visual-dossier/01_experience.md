# Release confidence

Build the agreed experience, verify the actual release, and preserve its evidence.
This is synthetic renderer input, not a report of a consumer release.

## Product decision

<div class="insight"><p>Use the reviewed prototype and user feedback as the acceptance baseline.</p></div>

::: callout-question
### What still needs proof?

The live flow must match the agreed behavior.
:::

| Outcome | State | Evidence |
|---|---|---|
| Local build | Accepted | Synthetic fixture |
| Live flow | Deferred | Not a deployed application |

## Release flow

```mermaid
flowchart TD
  accTitle: Evidence before release
  accDescr: Build the feature, verify it, then land the change.
  A[Build the feature] --> B[Verify behavior]
  B --> C[Land the change]
```

<!-- forge-include: parts/graph.md -->

## Next document

[Implementation record](02_implementation.md#handoff)
