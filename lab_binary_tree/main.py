from typing import Any, Callable
from graphviz import Digraph


class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value: Any) -> None:
        self.value = value
        self.left_child = None
        self.right_child = None

    def is_leaf(self) -> bool:
        if self.right_child and self.left_child:
            return False
        return True

    def add_left_child(self, value: Any) -> None:
        self.left_child = BinaryNode(value)

    def add_right_child(self, value: Any) -> None:
        self.right_child = BinaryNode(value)

    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        if self.left_child:
            self.left_child.traverse_in_order(visit)
        visit(self)
        if self.right_child:
            self.right_child.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]) -> None:
        if self.left_child:
            self.left_child.traverse_in_order(visit)
        if self.right_child:
            self.right_child.traverse_in_order(visit)
        visit(self)

    def traverse_pre_order(self, visit: Callable[[Any], None]) -> None:
        visit(self)
        if self.left_child:
            self.left_child.traverse_in_order(visit)
        if self.right_child:
            self.right_child.traverse_in_order(visit)

    def __str__(self) -> str:
        return str(self.value)


class BinaryTree:
    root: BinaryNode

    def __init__(self, value: Any) -> None:
        self.root = BinaryNode(value)

    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_in_order(visit)

    def traverse_pre_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_pre_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_post_order(visit)

    def show(self):
        tree = Digraph("tree")

        def add_to_graphviz_tree(node: 'BinaryNode'):
            if node.is_leaf:
                tree.edge(str(node.value), str(node.left_child.value))
                tree.edge(str(node.value), str(node.right_child.value))

        self.traverse_in_order(add_to_graphviz_tree)
        tree


treenode = BinaryNode(5)
print(treenode.is_leaf())
treenode.add_left_child(3)
treenode.add_right_child(8)
print(treenode.is_leaf())
treenode.traverse_in_order(print)
treenode.traverse_post_order(print)
treenode.traverse_pre_order(print)
binarytree = BinaryTree(treenode)
binarytree.show()





