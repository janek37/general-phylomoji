import math
from dataclasses import dataclass

import svgutils.transform as sg
import svgwrite
import svgwrite.path
import svgwrite.shapes

from constants import IMAGE_SIZE
from polar2cartesian import polar2cartesian
from tree_graph import Node, Leaf, Parent


@dataclass
class Positioner:
    position_count: int
    level_count: int
    tree_radius: float

    def get_radius(self, level: int) -> float:
        return (self.level_count - level) / self.level_count * self.tree_radius

    def get_angle(self, position: float):
        return position/self.position_count * 2*math.pi

    def get_coordinates(self, level: int, position: float):
        radius = self.get_radius(level=level)
        angle = self.get_angle(position=position)
        return polar2cartesian(radius=radius, angle=angle, center=(IMAGE_SIZE/2, IMAGE_SIZE/2))

    def get_node_coordinates(self, node: Node):
        return self.get_coordinates(level=node.level, position=node.position)


def render_tree(tree: Node, radius: float, stroke_width: float) -> sg.FigureElement:
    position_count = sum(1 for _ in tree.filter(lambda node: isinstance(node, Leaf)))
    drawing = svgwrite.Drawing(
        size=(IMAGE_SIZE, IMAGE_SIZE),
        profile='tiny',
    )
    positioner = Positioner(level_count=tree.level, position_count=position_count, tree_radius=radius)
    draw_levels(drawing=drawing, tree=tree, positioner=positioner, stroke_width=stroke_width)
    figure = sg.fromstring(drawing.tostring())
    return figure.getroot()


def draw_levels(drawing: svgwrite.Drawing, tree: Node, stroke_width: float, positioner: Positioner) -> None:
    if isinstance(tree, Parent):
        draw_level(
            drawing=drawing,
            parent=tree,
            positioner=positioner,
            stroke_width=stroke_width,
        )
        for child in tree.children:
            draw_levels(drawing=drawing, tree=child, positioner=positioner, stroke_width=stroke_width)


def draw_level(drawing: svgwrite.Drawing, parent: Parent, stroke_width: float, positioner: Positioner) -> None:
    path = make_main_path(parent, positioner, stroke_width)
    drawing.add(path)
    for child in parent.children[1:-1]:
        drawing.add(
            svgwrite.shapes.Line(
                start=positioner.get_coordinates(level=parent.level, position=child.position),
                end=positioner.get_coordinates(level=child.level, position=child.position),
                stroke='black',
                stroke_width=stroke_width,
            )
        )


def make_main_path(parent, positioner, stroke_width):
    parent_radius = positioner.get_radius(level=parent.level)
    first_child = parent.children[0]
    last_child = parent.children[-1]
    start = positioner.get_node_coordinates(node=first_child)
    end = positioner.get_coordinates(level=last_child.level, position=last_child.position)
    path = svgwrite.path.Path(
        stroke='black',
        stroke_width=stroke_width,
        fill='none',
    )
    path.push('M', *start)
    arc_start = positioner.get_coordinates(level=parent.level, position=first_child.position)
    path.push('L', *arc_start)
    if parent_radius != 0:
        make_arc(
            path=path,
            target=positioner.get_coordinates(level=parent.level, position=last_child.position),
            angle=positioner.get_angle(last_child.position - first_child.position),
            radius=parent_radius,
        )
    path.push('L', *end)
    return path


def make_arc(path, target, angle, radius):
    path.push_arc(target=target, rotation=0, r=radius, large_arc=angle > math.pi, absolute=True)
