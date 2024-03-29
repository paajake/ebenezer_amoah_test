import unittest
from versions_comparison import compare


class TestVersionsCompare(unittest.TestCase):
    def test_version_1_greater(self):
        self.assertEqual(compare("1", "0.0"), 1)
        self.assertEqual(compare("1", "-10"), 1)
        self.assertEqual(compare("10.2", "5.5.5"), 1)

    def test_versions_equal(self):
        self.assertEqual(compare("1", "1"), 0)
        self.assertEqual(compare("0.0.1", "0.0.1"), 0)
        self.assertEqual(compare("3.4", "3.4.0"), 0)

    def test_version_1_lesser(self):
        self.assertEqual(compare("0.0", "1"), -1)
        self.assertEqual(compare("0.0.1", "0.0.5"), -1)
        self.assertEqual(compare("3.4", "3.4.1"), -1)

    def test_args_types(self):
        with self.assertRaises(TypeError):
            compare("0.0")
        with self.assertRaises(TypeError):
            compare("0.1", "0.2", "0.3")
        with self.assertRaises(AttributeError):
            compare(1, "0.0")
        with self.assertRaises(ValueError):
            compare("0.1", "0.a")


if __name__ == '__main__':
    unittest.main()
