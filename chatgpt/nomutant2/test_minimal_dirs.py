import unittest
from minimal_dirs import minimal_dirs

class TestMinimalDirs(unittest.TestCase):
    def test_single_dir(self):
        self.assertEqual(minimal_dirs(["A"]), ["A"])

    def test_nested_dir(self):
        self.assertEqual(minimal_dirs(["A", "A/B"]), ["A"])

    def test_sibling_dirs(self):
        self.assertEqual(sorted(minimal_dirs(["A/B", "A/C"])),
                         ["A/B", "A/C"])

    def test_example_case(self):
        input_dirs = ["A/B", "A/B/C", "A/C/A", "A/C/B"]
        expected = ["A/B", "A/C/A", "A/C/B"]
        self.assertEqual(sorted(minimal_dirs(input_dirs)), sorted(expected))

    def test_deeply_nested(self):
        input_dirs = ["A/B", "A/B/C", "A/B/C/D"]
        expected = ["A/B"]
        self.assertEqual(minimal_dirs(input_dirs), expected)

    def test_unsorted_input(self):
        input_dirs = ["A/B/C", "A/B", "A/C/B", "A/C/A"]
        expected = ["A/B", "A/C/A", "A/C/B"]
        self.assertEqual(sorted(minimal_dirs(input_dirs)), sorted(expected))

if __name__ == "__main__":
    unittest.main()
