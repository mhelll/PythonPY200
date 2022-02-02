from typing import Any, Optional

class Node:
    def __init__(self, value: Any, next_: Optional["Node"] = None):
        self.value = value
        self.next = next_

    def __repr__(self) -> str:
        return f"Node({self.value}, {None})" if self.next is None else f"Node({self.value}, (Node({self.next}))"

    def __str__(self) -> str:
        return str(self.value)

    def is_valid(self, node: Any) -> None:
        if not isinstance(node, (type(None), Node)):
            raise TypeError

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_: Optional["Node"] = None) -> None:
        self.is_valid(next_)
        self._next = next_


class DoubleLinkedNode(Node):
    def __init__(self, value, next_, prev):
        super().__init__(value, next_)
        self.prev = prev

    def __repr__(self) -> str:
        next_= str(None) if self.next is None else f"{self.__class__.__name__}({self.next.value}), None, None"
        prev = str(None) if self.prev is None else f"{self.__class__.__name__}({self.prev.value}), None, None"
        return f"{self.__class__.__name__}, {next_, prev}"

    def __str__(self) -> str:
        self.prev = str.__str__

    @property
    def prev(self):
        return self.prev

    @prev.setter
    def prev(self, value):
        self.prev = value

if __name__ == "__main__":
    node1 = Node("Первый узел")
    node2 = Node("Второй узел")
    node3 = Node("Третий узел")

    node1.next = node2
    node2.next = node3

    node3.prev = node2
    node2.prev = node1
    print(repr(node1), repr(node1.next), repr(node2.next))
    print(repr(node3), repr(node3.prev), repr(node2.prev))