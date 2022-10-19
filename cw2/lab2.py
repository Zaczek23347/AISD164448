from typing import Any

class Node:
    value: Any
    next: 'Node'

    def __init__(self, value: Any):
        self.value = value
        self.next = None

class LinkedList:
    head: Node
    tail: Node

    def __init__(self):
        self.head = None
        self.tail = None

    def print(self):
        temp = self.head
        while(temp):
            if temp.next is None:
                print(temp.value)
            else:
                print(temp.value, "-> ", end="")
            temp = temp.next

    def len(self):
        length = 0
        temp = self.head
        while(temp):
            length += 1
            temp = temp.next
        return length

    def push(self, value: Any):
        new = Node(value)
        new.next = self.head
        self.head = new

    def append(self, value: Any):
        new = Node(value)
        if self.head is None:
            self.head = new
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = new

    def node(self, at: int):
        if (self.len()<at):
            print("zly index")

        else:
            new = Node(at)
            return new

    def insert(self, value: Any, after: Node):
        if after is None:
            print("zly index")

        else:
            new = Node(value)
            new.next = after.next
            after.next = new

    def pop(self):
        temp = self.head
        if temp is not None:
            self.head = temp.next
            temp = None

    def remove_last(self):
        temp = self.head
        while(temp.next):
            prev = temp
            temp = temp.next
        print(prev.next.value)
        prev.next = None

    def remove(self, after: Node):
        if after is None:
            print("zly index")

        else:
            after.next = None





list_ = LinkedList()
assert list_.head == None
list_.push(1)
list_.push(0)
list_.print()
list_.append(9)
list_.append(10)
list_.print()
middle_node = list_.node(at=1)
list_.insert(5, after=middle_node)
list_.print()
first_element = list_.node(at=0)
returned_first_element = list_.pop()
list_.print()
last_element = list_.node(at=3)
returned_last_element = list_.remove_last()
list_.print()
second_node = list_.node(at=1)
list_.remove(second_node)
list_.print()
