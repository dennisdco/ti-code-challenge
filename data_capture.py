# Team International Code challenge.
# Dennis Del Castillo (DDC).
# dennisdco@gmail.com

from binary_search_tree import BinarySearchTree

class DataCapture:
    def __init__(self):
        self.bst = BinarySearchTree()
    
    def add(self, val):
        try:
            value = float(val)
            print(value)
            if value > 0:
                self.bst.add(value)
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def less(self, val):
        return self.bst.get_lower_than(val)
    
    def greater(self, val):
        return self.bst.get_greater_than(val)
    
    def between(self, lower, upper):
        return self.bst.get_between_range(lower, upper)

    def build_stats(self):
        return self.bst