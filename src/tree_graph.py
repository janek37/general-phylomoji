from abc import ABC
from typing import List, Tuple, Union, Sequence

Tree = Union[str, Sequence["Tree"]]


class Node(ABC):
    def __init__(self, position: float, level: int):
        self.position = position
        self.level = level


class Leaf(Node):
    def __init__(self, position: float, value: str):
        super().__init__(position=position, level=0)
        self.value = value


class Parent(Node):
    def __init__(self, children: List[Node]):
        self.children = children
        super().__init__(position=self._get_position(), level=self._get_level())

    def _get_position(self) -> float:
        min_child_position = self.children[0].position
        max_child_position = self.children[-1].position
        return (min_child_position + max_child_position)/2

    def _get_level(self) -> int:
        max_child_level = max(child.level for child in self.children)
        return max_child_level + 1

    def leaf_count(self) -> int:
        return sum(
            child.leaf_count() if isinstance(child, Parent) else 1
            for child in self.children
        )


def make_graph(tree: Sequence[Tree]) -> Parent:
    tree_with_positions, _ = _add_positions(tree)
    return tree_with_positions


def _add_positions(tree: Sequence[Tree], start_position=0) -> Tuple[Parent, float]:
    position = start_position
    new_children = []
    for child in tree:
        if isinstance(child, str):
            new_child = Leaf(value=child, position=position)
            position += 1
        else:
            new_child, position = _add_positions(child, position)
        new_children.append(new_child)
    return Parent(children=new_children), position


if __name__ == '__main__':
    from life_emoji import BIRDS
    print(make_graph(BIRDS))
