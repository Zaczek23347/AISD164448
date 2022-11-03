from typing import Any, List
"aby zwizualizowac drzewo: biblioteka graphviz"

class TreeNode:
    value: Any
    children: List['TreeNode']

    def __init__(self, value ,children: List) -> None:
        self.value = value
        self.children = children
