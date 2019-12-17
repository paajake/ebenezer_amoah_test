import unittest
from versions_comparison import compare


class TestVersionsCompare(unittest.TestCase):
    def test_vesrsion_1_greater(self):
        self.assertEqual(compare("1", "0.0"), 1)
        self.assertEqual(compare("1", "-10"), 1)
        self.assertEqual(compare("10.2", "5.5.5"), 1)

    def test_vesrsions_equal(self):
        self.assertEqual(compare("1", "1"), 0)
        self.assertEqual(compare("0.0.1", "0.0.1"), 0)
        self.assertEqual(compare("3.4", "3.4.0"), 0)

    def test_vesrsion_1_lesser(self):
        self.assertEqual(compare("0.0", "1"), -1)
        self.assertEqual(compare("0.0.1", "0.0.5"), -1)
        self.assertEqual(compare("3.4", "3.4.1"), -1)


if __name__ == '__main__':
    unittest.main()
