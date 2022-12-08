from __future__ import annotations
from typing import Any



class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value: Any) -> None:
        self.value = value
        self.left_child = None
        self.right_child = None

    def min(self) -> BinaryNode:
        minnode = self
        if self.left_child < minnode.value:
            minnode = self.left_child
            self.left_child.min()
        return minnode

class BinarySearchTree:
    root: BinaryNode

    def insert(self, value: Any) -> None:
        newroot = self._insert(self, value)
        self.root = newroot

    def _insert(self, node: BinaryNode, value: Any) -> BinaryNode:
        if value < node.value:
            node.left_child = node._insert(node.left_child, value)
        if value > node.value:
            node.right_child = node._insert(node.right_child, value)
        return node

    def insert_list(self, list_: List[Any]) -> None:
        for x in list_:
            self.insert(x)

    def contains(self, value: Any) -> bool:
        node = self
        node.insert(value)
        if node == self:
            return True
        return False


