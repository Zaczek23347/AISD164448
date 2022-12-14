from __future__ import annotations
from typing import Any, List
import graphviz


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

    def __init__(self, root: 'BinaryNode') -> None:
        self.root = root

    def insert(self, value: Any) -> None:
        self.root = self._insert(self.root, value)

    def _insert(self, node: BinaryNode, value: Any) -> BinaryNode:
        if value < node.value:
            if node.left_child is not None:
                self._insert(node.left_child, value)
            else:
                node.left_child = BinaryNode(value)
        else:
            if node.right_child is not None:
                self._insert(node.right_child, value)
            else:
                node.right_child = BinaryNode(value)
        return node

    def insert_list(self, list_: List[Any]) -> None:
        for x in list_:
            self.insert(x)

    def contains(self, value: Any) -> bool:
        node = self.root
        while node is not None:
            if value == node.value:
                return True
            if value < node.value:
                node = node.left_child
            else:
                node = node.right_child
        return False

    def remove(self, value: Any) -> None:
        self.root = self._remove(self.root, value)

    def _remove(self, node: BinaryNode, value: Any) -> BinaryNode:
        if value == node.value:
            if node.left_child is None and node.right_child is None:
                return None
            if node.left_child is None:
                return node.right_child
            if node.right_child in None:
                return node.left_child
            node.value = node.min()
            node.right_child = node._remove(node.right_child, value)
            if value < node.value:
                node.left_child = node._remove(node.left_child, value)
            if value > node.value:
                node.right_child = node._remove(node.right_child, value)
            return node

    def show(self) -> None:
        tree = graphviz.Digraph(name='Drzewo')
        stack = [self.root]
        while stack:
            node = stack.pop()
            if node is not None:
                if node.left_child is not None:
                    tree.edge(str(node.value), str(node.left_child.value))
                    stack.append(node.left_child)
                if node.right_child is not None:
                    tree.edge(str(node.value), str(node.right_child.value))
                    stack.append(node.right_child)
        tree.render('tree.gv', view=True)

drzewo: BinarySearchTree = BinarySearchTree(BinaryNode(8))

drzewo.insert(3)
drzewo.insert(10)
drzewo.insert(1)
drzewo.insert(6)
drzewo.insert(4)
drzewo.insert(7)
drzewo.insert(14)
drzewo.insert(13)


drzewo.show()

