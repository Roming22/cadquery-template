import cadquery as cq

from parts import box, cylinder


def build(name: str) -> cq.Assembly:
    """Assemble the parts into the final assembly."""
    box_part = box.build(cq.Workplane("XY"))
    cyl = cylinder.build(cq.Workplane("XY"))

    result = cq.Assembly(name=name)
    result.add(box_part, name=box.NAME)
    result.add(cyl, name=cylinder.NAME, loc=cq.Location(cq.Vector(0, 0, 0)))

    return result
