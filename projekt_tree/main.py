from typing import Any, List, Callable, Union
import queue as q
import graphviz



class TreeNode:
    value: Any
    children: List['TreeNode']

    def __init__(self, value: Any) -> None:
        self.value = value
        self.children = []

    def is_leaf(self) -> bool:
        if not self.children:
            return True
        else:
            return False

    def add(self, child: 'TreeNode') -> None:
        self.children.append(child)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)
        for child in self.children:
            child.for_each_deep_first(visit)

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)
        fifo = q.Queue()
        for child in self.children:
            fifo.put(child)
            while fifo.qsize() != 0:
                fifo2 = fifo.get(child)
                visit(fifo2)
                for grandchild in fifo2.children:
                    fifo.put(grandchild)

    def search(self, value: Any) -> Union['TreeNode', None]:
        if self.value == value:
            return self
        for child in self.children:
          #  t = child.search(value)
           # if t != None: 
            #     return t //wszystko ponizej usunac 
            if child.value == value:
                child.search(value)
                return child

    def __str__(self) -> str:
        return str(self.value)


class Tree:
    root: TreeNode

    def __init__(self, value: Any) -> None:
        self.root = TreeNode(value)

    def add(self, value: Any, parent_name: Any) -> None:
        parent = self.root.search(parent_name)
        parent.add(TreeNode(value))

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        self.root.for_each_level_order(visit)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        self.root.for_each_deep_first(visit)

    def show(self):
        tree = graphviz.Digraph("tree")

        def add_to_graphviz_tree(node: 'TreeNode'):
            for child in node.children:
                tree.edge(str(node.value), str(child.value))

        self.for_each_deep_first(add_to_graphviz_tree)
        tree.view()




treenode = TreeNode("F")


tree = Tree(treenode)
tree.add("B", treenode)
tree.add("G", treenode)
tree.add("A", "B")
tree.add("D", "B")
tree.add("I", "G")


tree.for_each_level_order(print)

tree.show()
