# CadQuery Part Template

A small starter project for designing parametric CAD parts with [CadQuery](https://cadquery.readthedocs.io/). 

The sample model is a simple piece made out of 2 parts.

## Develop in a container

This project is set up for [Dev Containers](https://containers.dev/). Open the folder in Cursor or VS Code and reopen in the container when prompted (or run **Dev Containers: Reopen in Container**).

The image is Python 3.12 with CadQuery and the OpenGL libraries OCP needs. You do not need a local CadQuery install — build and export inside the container.

## Using with Cursor

If you use [Cursor](https://cursor.com/), we recommend installing [flowful-ai/cad-skill](https://github.com/flowful-ai/cad-skill). It steers the agent through parametric CadQuery modeling, STL export, preview rendering, and printability checks.

```bash
mkdir -p ~/.cursor/skills
git clone https://github.com/flowful-ai/cad-skill ~/.cursor/skills/parametric-3d-printing
```

After that, describe the part you want (enclosure, bracket, Gridfinity bin, and so on) and let the agent iterate on the model in this repo.

## Project layout

| Path | Purpose |
|------|---------|
| `src/parts/` | Part geometry and part-specific dimensions |
| `src/_common.py` | Dimensions shared across parts / assembly |
| `src/assembly.py` | Combines parts into the root assembly |
| `src/main.py` | Runs the assembly and exports GLB/STL |
| `output/` | Generated model files |

## Quick start

With the Dev Container running:

```bash
python src/main.py
```

That writes the models named by `NAME` in `main.py` (default: `output/part.stl` / `.glb`). Use the **Run** launch configuration to do the same from the debugger.

## Designing a part

1. Set part-specific sizes in the relevant `src/parts/` module (shared sizes in `src/_common.py`)
2. Add or edit geometry helpers in `src/parts/`
3. Wire them into `build = pipe(...)`, and place parts in `src/assembly.py`
4. Run `python src/main.py` and inspect the models in `output/`

Keep dimensions in millimeters. Prefer named parameters over magic numbers in the geometry code.
