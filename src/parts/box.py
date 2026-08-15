import cadquery as cq

from _common import WALL_THICKNESS

# =============================================================================
# IDENTITY / APPEARANCE
# =============================================================================

NAME = "box"
# CadQuery named color (or an (r, g, b[, a]) tuple with channels in 0–1)
COLOR = "lightblue"

# =============================================================================
# DIMENSIONS (mm)
# =============================================================================

LENGTH = 130.0   # X
WIDTH = 80.0    # Y
HEIGHT = 50.0   # Z

INNER_LENGTH = LENGTH - (2.0 * WALL_THICKNESS)
INNER_WIDTH = WIDTH - (2.0 * WALL_THICKNESS)
INNER_DEPTH = HEIGHT - WALL_THICKNESS  # floor = wall thickness


# =============================================================================
# GEOMETRY HELPERS (pure transforms: Workplane -> Workplane)
# =============================================================================

def create_base_profile(plane: cq.Workplane) -> cq.Workplane:
    """Draws the outer closed 2D rectangular profile."""
    return plane.rect(LENGTH, WIDTH)


def extrude_body(profile: cq.Workplane) -> cq.Workplane:
    """Extrudes the solid outer shell."""
    return profile.extrude(HEIGHT)


def cut_interior(part: cq.Workplane) -> cq.Workplane:
    """Hollows the bin, leaving WALL_THICKNESS on sides and floor."""
    return (
        part
        .faces(">Z")
        .workplane()
        .rect(INNER_LENGTH, INNER_WIDTH)
        .extrude(-INNER_DEPTH, combine="cut")
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
    create_base_profile,
    extrude_body,
    cut_interior,
    as_colored_assembly,
)
