Manual CSV concatenation was rejected because quoting semantics are easy to
break. A new third-party CSV library adds a dependency without a required benefit.
Use the standard library and test round-trip behavior with an independent reader.
