import math
from typing import Sequence, Iterable, Tuple, List

import svgutils.transform as sg

from constants import IMAGE_SIZE
from emoji_sources import EmojiSource
from polar2cartesian import polar2cartesian


def get_emoji_elements(
    emoji_list: Sequence[str],
    emoji_source: EmojiSource,
    emoji_size: float,
    emoji_radius: float,
) -> Iterable[sg.FigureElement]:
    vertices = _regular_polygon_vertices(
        n=len(emoji_list),
        r=emoji_radius,
        center=(IMAGE_SIZE / 2, IMAGE_SIZE / 2)
    )

    for i, ((x, y), emoji) in enumerate(zip(vertices, emoji_list)):
        emoji_svg = emoji_source.get_emoji_svg(emoji)
        # fix for noto ids
        fixed_emoji_svg = emoji_svg.replace('SVGID_', f'SVGID_{i}_')
        emoji_fig = sg.fromstring(fixed_emoji_svg)
        emoji_element = emoji_fig.getroot()
        emoji_element.scale(emoji_size / emoji_source.size)
        emoji_element.moveto(x - emoji_size / 2, y - emoji_size / 2)
        yield emoji_element


def _regular_polygon_vertices(n: int, r: float, center: Tuple[float, float]) -> List[Tuple[float, float]]:
    return [
        polar2cartesian(radius=r, angle=2 * math.pi * i / n, center=center)
        for i in range(n)
    ]
