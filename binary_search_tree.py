# Team International Code challenge.
# Dennis Del Castillo (DDC).
# dennisdco@gmail.com

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __iter__(self):
        return self._inorder_iterator(self.root)

    class _inorder_iterator:
        def __init__(self, node):
            self.stack = []
            self.current = node

        def __iter__(self):
            return self

        def __next__(self):
            while self.stack or self.current:
                if self.current:
                    self.stack.append(self.current)
                    self.current = self.current.left
                else:
                    node = self.stack.pop()
                    self.current = node.right
                    return node.val
            raise StopIteration

    def add(self, val):
        if val <= 0:
            raise ValueError("Please provide a positive number.")
        self.root = self._add(self.root, val)

    def _add(self, node, val):
        if node is None:
            return Node(val)
        if val <= node.val:
            node.left = self._add(node.left, val)
        elif val > node.val:
            node.right = self._add(node.right, val)
        return node

    def get_greater_than(self, val):
        result = []
        self._get_greater_than(self.root, val, result)
        result.sort()
        return result

    def _get_greater_than(self, node, val, result):
        if node is None:
            return
        if node.val > val:
            result.append(node.val)
            self._get_greater_than(node.left, val, result)
            self._get_greater_than(node.right, val, result)
        elif node.val == val:
            self._get_greater_than(node.right, val, result)
        else:
            self._get_greater_than(node.right, val, result)

    def get_lower_than(self, val):
        result = []
        self._get_lower_than(self.root, val, result)
        result.sort()
        return result

    def _get_lower_than(self, node, val, result):
        if node is None:
            return
        if node.val < val:
            result.append(node.val)
            self._get_lower_than(node.left, val, result)
            self._get_lower_than(node.right, val, result)
        elif node.val == val:
            self._get_lower_than(node.left, val, result)
        else:
            self._get_lower_than(node.left, val, result)

    def get_between_range(self, lower, upper):
        result = []
        self._get_between_range(self.root, lower, upper, result)
        result.sort()
        return result

    def _get_between_range(self, node, lower, upper, result):
        if node is None:
            return
        if lower <= node.val <= upper:
            result.append(node.val)
            self._get_between_range(node.left, lower, upper, result)
            self._get_between_range(node.right, lower, upper, result)
        elif node.val == lower:
            self._get_between_range(node.right, lower, upper, result)
        elif node.val == upper:
            self._get_between_range(node.left, lower, upper, result)
        elif node.val > upper:
            self._get_between_range(node.left, lower, upper, result)
        else:
            self._get_between_range(node.right, lower, upper, result)
