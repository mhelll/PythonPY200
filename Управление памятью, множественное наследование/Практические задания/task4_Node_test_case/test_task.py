import unittest

from task import Node


class TestCase(unittest.TestCase):  # TODO наследоваться от unittest.TestCase
    def test_init_node_without_next(self):
        """Проверить следующий узел после инициализации с аргументом next_ по умолчанию"""
        node = Node(5)  # TODO с помощью метода assertIsNone проверить следующий узел

        # self.assertIs(None, node.next)
        self.assertIsNone(node.next)
        # self.assertEqual(10, node.value)

    def test_init_node_with_next(self):
        """Проверить следующий узел после инициализации с переданным аргументом next_"""
        right_node = Node("right_node")  # TODO проверить что узлы связались
        left_node = Node("left_node", next_=right_node)

        self.assertIs(right_node, left_node.next)
        self.assertEqual("left_node", left_node.value)

        self.assertIsNone(right_node.next)
        self.assertEqual("right_node", right_node.value)

    def test_repr_node_without_next(self):
        """Проверить метод __repr__, для случая когда нет следующего узла."""
        node = Node(5)  # TODO проверить метод __repr__ без следующего узла

        expected_repr = "Node(5, None)"
        self.assertEqual(expected_repr, repr(node))


    @unittest.skip("Будет дорабатываться")  # TODO пропустить тест с помощью декоратора unittest.skip
    def test_repr_node_with_next(self):
        """Проверить метод __repr__, для случая когда установлен следующий узел."""
        node = Node(5, Node(10))

        expected_repr = "Node(5, None(10)"
        self.assertEqual(expected_repr, repr(node))

    def test_str(self):
        some_value = 5
        node = Node(some_value)

        self.assertEqual(str(some_value), str(node))    # TODO проверить строковое представление

    def test_is_valid(self):
        Node.is_valid(Node("some_value"))  # TODO проверить метод is_valid при корректных узлах
        Node.is_valid(None)

        with self.assertRaises(TypeError, msg="Должна быть вызвана ошибка TypeError"):
            Node.is_valid(None)    # TODO с помощью менеджера контакста и метода assertRaises проверить корректность вызываемой ошибки
