from typing import Any, Iterable, Optional
from collections.abc import MutableSequence
from node import Node, DoubleLinkedNode


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

        if not 0 <= index < self.len:
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
        node = self.step_by_step_on_nodes(index)
        node.value = value

    def __delitem__(self, key):
        del self.__dict__[key]

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
                print("Элемента нет в списке")
            else:
                new_node = Node(value)
                new_node.prev = node
                new_node.next = node.next
                if node.next is not None:
                    node.next.prev = new_node
                node.next = new_node

    def remove(self, remove_value: Any) -> None:
        """
        1. Через enumerate от self получать пару индекс-значение. Описать через какой магический метод работает for ... in ...
        2. Через встроенную функцию del удалить по индексу элемент. Разобраться как работает магический метод
        3. Написать тесты
        :param remove_value:
        :return:
        """
        ...

class DoubleLinkedList(LinkedList):
    node_class = DoubleLinkedNode

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        left_node.next = right_node
        right_node.prev = left_node


if __name__ == "__main__":
    ll1 = LinkedList([1, 2, 3, 4, 5])
    ll1.append(6)
    ll1.insert(3, 77)
    ll1.step_by_step_on_nodes(4)
    print(ll1)

    ll2 = DoubleLinkedList([1, 2, 3])
    ll2.append(6)
    ll2.append(1)
    ll2.insert(6, 777)
    print(ll2)
