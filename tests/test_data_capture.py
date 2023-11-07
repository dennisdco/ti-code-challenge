# Team International Code challenge.
# Dennis Del Castillo (DDC).
# dennisdco@gmail.com

import unittest
from data_capture import DataCapture

class TestDataCapture(unittest.TestCase):
    def setUp(self):
        self.capture = DataCapture()
        self.stats = self.capture.build_stats()
        self.capture.add(3)
        self.capture.add(9)
        self.capture.add(3)
        self.capture.add(4)
        self.capture.add(6)

    def test_add(self):
        self.assertEqual(list(self.capture.bst), [3, 3, 4, 6, 9])

    def test_lower_than(self):
        less_than = self.stats.get_lower_than(4)
        self.assertEqual(less_than, [3, 3])
    
    def test_greater_than(self):
        greater_than = self.stats.get_greater_than(4)
        self.assertEqual(greater_than, [6, 9])
        
    def test_between_range(self):
        result = self.stats.get_between_range(3, 6)
        self.assertEqual(result, [3, 3, 4, 6])

if __name__ == '__main__':
    unittest.main()
