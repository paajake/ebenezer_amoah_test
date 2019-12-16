import unittest
from overlap import is_overlaping

class TestOverlap(unittest.TestCase):
    def test_lines_overlap(self):
        self.assertEqual( is_overlaping ((0, 10), (2, 15)), True)
        self.assertEqual( is_overlaping ((10, 25), (5, 16)), True)
        self.assertEqual( is_overlaping ((20, 25), (10, 30)), True)
    
    def test_lines_dont_overlap(self):
        self.assertEqual( is_overlaping ((0, 10), (10.1, 15)), False)
        self.assertEqual( is_overlaping ((-12, -5), (0, 10)), False)
        self.assertEqual( is_overlaping ((-10, 0.0), (0.0, 10)), False)
    
    def test_lines_types(self):
       with self.assertRaises(TypeError): is_overlaping((9,15), "overlap")
       with self.assertRaises(TypeError): is_overlaping("text", (12,21))
       with self.assertRaises(TypeError): is_overlaping((9,15), ("12",20))

if __name__ == '__main__':
    unittest.main()