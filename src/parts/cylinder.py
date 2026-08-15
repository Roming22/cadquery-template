import cadquery as cq

from _common import WALL_THICKNESS

# =============================================================================
# IDENTITY / APPEARANCE
# =============================================================================

NAME = "tube"
# CadQuery named color (or an (r, g, b[, a]) tuple with channels in 0–1)
COLOR = "red"

# =============================================================================
# DIMENSIONS (mm)
# =============================================================================

RADIUS = 20.0
HEIGHT = 60.0
INNER_RADIUS = RADIUS - WALL_THICKNESS


# =============================================================================
# GEOMETRY HELPERS (pure transforms: Workplane -> Workplane)
# =============================================================================

def create_tube(plane: cq.Workplane) -> cq.Workplane:
    """Hollow tube with bottom on the workplane (Z=0)."""
    return (
        plane
        .circle(RADIUS)
        .circle(INNER_RADIUS)
        .extrude(HEIGHT)
    )


def as_colored_assembly(part: cq.Workplane) -> cq.Assembly:
    """Wraps the solid in a named assembly with COLOR."""
    return cq.Assembly(part, name=NAME, color=cq.Color(COLOR))


def pipe(*fns):
    """Left-to-right function composition: pipe(f, g, h)(x) == h(g(f(x)))."""
    def piped(x):
        for fn in fns:
            x = fn(x)
        return x
    return piped


# =============================================================================
# MODEL CONSTRUCTION
# =============================================================================

build = pipe(
    create_tube,
    as_colored_assembly,
)
