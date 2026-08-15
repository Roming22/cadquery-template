# =============================================================================
# MAIN
# =============================================================================
NAME = "part"

from pathlib import Path

import cadquery as cq

import assembly


result = assembly.build(NAME)

# Export the assembly
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# glb has color information, stl does not
result.export(str(OUTPUT_DIR / f"{NAME}.glb"))
cq.exporters.export(result.toCompound(), str(OUTPUT_DIR / f"{NAME}.stl"))
