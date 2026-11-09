# Style

- Indent: 2 spaces, no tabs.
- Line length: 57 symbol.
- Quotes: single quotes for code, f-strings for interpolation.
- Naming: `snake_case` for functions/variables, `UPPER_SNAKE` for module constants,
  `Final` type hints on command tuples.
- Type hints required on public helpers; entry points may omit them.
- Docstrings: one-line summary on public functions.
- Command groups are public tuples (`MODE_*`, `EXIT_CMDS`, …) — do not mutate.
- I/O is isolated in `main()`; quiz logic lives in pure/session functions.
- Inputs are lowercased once at the edge, then compared.
