# Team International Code challenge.
# Dennis Del Castillo (DDC).
# dennisdco@gmail.com

import unittest
from binary_search_tree import BinarySearchTree

class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def test_add(self):
        self.bst.add(10)
        self.assertEqual(self.bst.root.val, 10)

        self.bst.add(5)
        self.assertEqual(self.bst.root.val, 10)
        self.assertEqual(self.bst.root.left.val, 5)

        self.bst.add(15)
        self.assertEqual(self.bst.root.val, 10)
        self.assertEqual(self.bst.root.left.val, 5)
        self.assertEqual(self.bst.root.right.val, 15)

    def test_get_greater_than(self):
        self.bst.add(10)
        self.bst.add(5)
        self.bst.add(15)
        self.bst.add(3)
        self.bst.add(7)
        self.bst.add(12)

        result = self.bst.get_greater_than(8)
        self.assertEqual(result, [10, 12, 15])

    def test_get_lower_than(self):
        self.bst.add(10)
        self.bst.add(5)
        self.bst.add(15)
        self.bst.add(3)
        self.bst.add(7)
        self.bst.add(12)

        result = self.bst.get_lower_than(8)
        self.assertEqual(result, [3, 5, 7])

    def test_get_between_range(self):
        self.bst.add(10)
        self.bst.add(5)
        self.bst.add(15)
        self.bst.add(3)
        self.bst.add(7)
        self.bst.add(12)

        result = self.bst.get_between_range(6, 14)
        self.assertEqual(result, [7, 10, 12])

if __name__ == '__main__':
    unittest.main()
