# Agent guidelines

## Parameters

All magic numbers must be declared as named constants.

- Do not hard-code dimensions, clearances, counts, or other numeric literals inline in geometry or assembly logic.
- Part-specific dimensions live in that part’s module under `src/parts/`.
- Dimensions shared by more than one part or by the assembly live in `src/_common.py`.
- Keep units in millimeters; document units in comments next to the parameter definitions.
- Part names and colors are not magic numbers; keep them with the part (e.g. `NAME` / `COLOR` in `parts/box.py` / `parts/cylinder.py`). The root assembly export name lives in `main.py` as `NAME`.
