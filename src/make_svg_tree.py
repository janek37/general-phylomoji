import math
import os
from typing import Iterator, Sequence

from compose_svg import compose_svg
from emoji_sources import NOTO_EMOJI, TWEMOJI, OPENMOJI, EmojiSource
from get_emoji_elements import get_emoji_elements
from life_emoji import BIRDS, CARNIVORANS, UNGULATA, MAMMALS, ANIMALS, PLANTS, LIFE_EMOJI
from constants import MAX_EMOJI_SIZE, MAX_EMOJI_DENSITY, IMAGE_SIZE, EMOJI_MARGIN, RELATIVE_STROKE_WIDTH
from render_tree import render_tree
from tree_graph import make_graph, Tree


def flatten_tree(tree: Tree) -> Iterator[str]:
    if isinstance(tree, str):
        yield tree
    elif isinstance(tree, Sequence):
        for child in tree:
            yield from flatten_tree(child)


def get_emoji_size(emoji_count: int) -> float:
    return min(MAX_EMOJI_SIZE, math.pi*IMAGE_SIZE/emoji_count*MAX_EMOJI_DENSITY)


def get_emoji_radius(emoji_size: float) -> float:
    return IMAGE_SIZE/2 - emoji_size/2*(1+EMOJI_MARGIN)


def get_tree_radius(emoji_size: float, emoji_radius: float) -> float:
    return emoji_radius - emoji_size/2*(1+EMOJI_MARGIN)


def make_svg_tree(tree: Tree, emoji_source: EmojiSource, filename: str):
    emoji_list = list(flatten_tree(tree))
    emoji_size = get_emoji_size(len(emoji_list))
    emoji_radius = get_emoji_radius(emoji_size)
    stroke_width = emoji_size * RELATIVE_STROKE_WIDTH
    emoji_elements = list(
        get_emoji_elements(
            emoji_list=emoji_list,
            emoji_source=emoji_source,
            emoji_size=emoji_size,
            emoji_radius=emoji_radius,
        )
    )
    tree_radius = get_tree_radius(emoji_size=emoji_size, emoji_radius=emoji_radius)
    tree_graph = make_graph(tree=tree)
    rendered_tree = render_tree(tree=tree_graph, radius=tree_radius, stroke_width=stroke_width)
    emoji_elements.append(rendered_tree)
    fig = compose_svg(emoji_elements)
    fig.save(filename)


def main():
    sources_directories = [
        (NOTO_EMOJI, 'trees-noto'),
        (TWEMOJI, 'trees-twemoji'),
        (OPENMOJI, 'trees-openmoji'),
    ]
    trees_filenames = [
        (BIRDS, 'birds.svg'),
        (CARNIVORANS, 'carnivorans.svg'),
        (UNGULATA, 'ungulata.svg'),
        (MAMMALS, 'mammals.svg'),
        (ANIMALS, 'animals.svg'),
        (PLANTS, 'plants.svg'),
        (LIFE_EMOJI, 'life.svg'),
    ]
    for emoji_source, directory in sources_directories:
        for tree, filename in trees_filenames:
            os.makedirs(directory, exist_ok=True)
            make_svg_tree(emoji_source.filter_tree(tree), emoji_source, os.path.join(directory, filename))


if __name__ == '__main__':
    main()
