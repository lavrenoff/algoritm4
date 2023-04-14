# Собрать полноценное левостороннее красно-черное дерево.
# И реализовать в нем метод добавления новых элементов с балансировкой.
import random


class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.color = 'R'


class LeftRBTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if not self.root:
            self.root = Node(value)
            self.root.color = 'B'
        else:
            self.root = self._add(value, self.root)
            self.root.color = 'B'

    def _add(self, value, node):
        if not node:
            return Node(value)
        elif value < node.value:
            node.left = self._add(value, node.left)
        else:
            node.right = self._add(value, node.right)
        if self._is_red(node.right) and not self._is_red(node.left):
            node = self._rotate_left(node)
        if self._is_red(node.left) and self._is_red(node.left.left):
            node = self._rotate_right(node)
        if self._is_red(node.left) and self._is_red(node.right):
            self._swap_colors(node)
        return node

    def _is_red(self, node):
        if not node:
            return False
        return node.color == 'R'

    def _rotate_left(self, node):
        x = node.right
        node.right = x.left
        x.left = node
        x.color = node.color
        node.color = 'R'
        return x

    def _rotate_right(self, node):
        x = node.left
        node.left = x.right
        x.right = node
        x.color = node.color
        node.color = 'R'
        return x

    def _swap_colors(self, node):
        node.color = 'R' if node.color == 'B' else 'B'
        node.left.color = 'B'
        node.right.color = 'B'


def print_rb_tree(node, level=0):
    if node is None:
        return
    print("-" * level, end="")
    print("[" + str(node.value) + "]" + (" RED" if node.color == "R" else " BLACK"))
    print_rb_tree(node.left, level + 1)
    print_rb_tree(node.right, level + 1)


tree = LeftRBTree()

for i in range(20):
    tree.add(random.randint(1, 10000))

print_rb_tree(tree.root)