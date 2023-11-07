# TI Code challenge

## Problem
The DataCapture object should accept numbers and returns an object for querying statistics about the inputs. Specifically, the returned object supports querying how many numbers in the collection are less than a value, greater than a value, or within a range. All this operations should have a constant time.

## Solution 
### Bynary Search Tree
A binary search tree (BST) is a data structure used for organizing and storing a set of elements. It is a type of binary tree with the following properties:

**Binary Tree Structure:** Each node in a binary search tree has at most two children, referred to as the left child and the right child.

**Ordering Property:** For every node N, all elements in the left subtree of N are less than N, and all elements in the right subtree of N are greater than N. This property ensures that the elements are ordered, making it easy to perform efficient searches.

Because of these properties, binary search trees are particularly useful for tasks like searching for a specific element, inserting new elements, and deleting elements efficiently.

Here's an example of a binary search tree:
```
       8
      / \
     3   10
    / \    \
   1   6    14
      / \   /
     4   7  13
```
Using this structure we can achieve a time complexity of O(n)

## Alternative Solution
### Use an AVL Tree with ```sortedcontainers``` library
We can achieve an improved result using an AVL Tree which provides efficient insertion, deletion, and search operations with a time complexity of O(log n) in the average and worst case.
We can achieve this by using [sortedcontainers](https://pypi.org/project/sortedcontainers/0.8.4/)
Which can reduce the implementation to:

```
from sortedcontainers import SortedDict
class AVLTree:
    def __init__(self):
        self.data = SortedDict()

    def add(self, num):
        if num > 0:
            self.data[num] = None

    def get_greater_than(self, num):
        return list(key for key in self.data.keys() if key > num)

    def get_lower_than(self, num):
        return list(key for key in self.data.keys() if key < num)

    def get_between_range(self, lower, upper):
        return list(key for key in self.data.keys() if lower < key < upper)
```

## How to run the examples:
You can run this examples by using a Python virtual environment or executing the main module ```main.py```



