from typing import Iterable

import svgutils.transform as sg
from svgutils.compose import Unit

from constants import IMAGE_SIZE


def compose_svg(svg_elements: Iterable[sg.FigureElement]) -> sg.SVGFigure:
    figure = sg.SVGFigure(width=Unit(str(IMAGE_SIZE)), height=Unit(str(IMAGE_SIZE)))

    for svg_element in svg_elements:
        figure.append(svg_element)
    return figure
