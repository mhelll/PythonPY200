from typing import Any, Iterable, Optional
from collections.abc import MutableSequence
from node import Node

class LinkedList(MutableSequence):
    node_class = Node

    def __init__(self, value: Iterable = None):
        self.len = 0
        self.head: Optional[Node] = None
        self.tail = self.head

        if value is not None:
            for value in value:
                self.append(value)

    def append(self, value: Any):
        append_node = self.node_class(value)

        if self.head is None:
            self.head = self.tail = append_node
        else:
            self.linked_nodes(self.tail, append_node)
            self.tail = append_node

        self.len += 1

    def step_by_step_on_nodes(self, index: int) -> Node:
        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self.len:  # для for
            raise IndexError()

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        left_node.next = right_node

    def __getitem__(self, index):
        node = self.step_by_step_on_nodes(index)
        return node.value

    def __setitem__(self, value, index):
        """ Метод устанавливает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        node.value = value

    def __delitem__(self, index):
        if self.head is None:
            print("В списке нет элемента для удаления")
            return
        if self.head.next is None:
            if self.head.value == index:
                self.head = None
            else:
                print("Элемент не найден")
            return
        if self.head.value == index:
            self.head = self.head.next
            self.head.prev = None
            return

        node = self.head
        while node.next is not None:
            if node.value == index:
                break
            node = node.next
        if node.next is not None:
            node.prev.next = node.next
            node.next.prev = node.prev
        else:
            if node.value == index:
                node.prev.next = None
            else:
                print("Элемент не найден")

    def __len__(self) -> int:
        return self.len

    def to_list(self) -> list:
        return [linked_list_value for linked_list_value in self]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_list()})"

    def __str__(self) -> str:
        return f"{self.to_list()}"

    def insert(self, index: int, value) -> None:
        if self.head is None:
            print("Список пусто")
            return
        else:
            node = self.head
            while node is not None:
                if node.value == index:
                    break
                node = node.next
            if node is None:
                print("item not in the list")
            else:
                new_node = Node(value)
                new_node.prev = node
                new_node.next = node.next
                if node.next is not None:
                    node.next.prev = new_node
                node.next = new_node



class DoubleLinkedList(LinkedList):
    ...


if __name__ == "__main__":
    ll = LinkedList