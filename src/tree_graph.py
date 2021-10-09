from dataclasses import dataclass
from typing import Optional, List, Callable, Iterable, Tuple, Union, Sequence

Tree = Union[str, Sequence["Tree"]]


@dataclass
class Node:
    position: Optional[float] = None
    level: Optional[int] = None

    def filter(self, test: Callable[["Node"], bool]) -> Iterable["Node"]:
        if test(self):
            yield self


@dataclass
class Leaf(Node):
    level: Optional[float] = 0
    value: str = NotImplemented


@dataclass
class Parent(Node):
    children: List["Node"] = NotImplemented

    def __post_init__(self):
        self.position = self._get_position()
        self.level = self._get_level()

    def _get_position(self) -> float:
        child_positions = [child.position for child in self.children]
        assert None not in child_positions
        min_child_position = min(child_positions)
        max_child_position = max(child_positions)
        return (min_child_position + max_child_position)/2

    def _get_level(self) -> int:
        max_child_level = max(child.level for child in self.children)
        return max_child_level + 1

    def filter(self, test: Callable[[Node], bool]):
        yield from super().filter(test)
        for child in self.children:
            yield from child.filter(test)


def make_graph(tree: Tree) -> Node:
    tree_with_positions, _ = _add_positions(tree)
    return tree_with_positions


def _add_positions(tree: Tree, start_position=0) -> Tuple[Node, float]:
    position = start_position
    if isinstance(tree, str):
        return Leaf(value=tree, position=position), position + 1
    else:
        new_children = []
        for child in tree:
            new_child, position = _add_positions(child, position)
            new_children.append(new_child)
        return Parent(children=new_children), position


if __name__ == '__main__':
    from life_emoji import BIRDS
    print(make_graph(BIRDS))
