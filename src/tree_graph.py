from typing import List, Callable, Iterable, Tuple, Union, Sequence

Tree = Union[str, Sequence["Tree"]]


class Node:
    def __init__(self, position: float, level: int):
        self.position = position
        self.level = level

    def filter(self, test: Callable[["Node"], bool]) -> Iterable["Node"]:
        if test(self):
            yield self


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
