import unittest
from minimal_dirs import minimal_dirs

class TestMinimalDirs(unittest.TestCase):
    def test_single_dir(self):
        self.assertEqual(minimal_dirs(["A"]), ["A"])

    def test_two_dirs_one_subdir(self):
        self.assertEqual(minimal_dirs(["A/B", "A/B/C"]), ["A/B"])

    def test_multiple_dirs_no_overlap(self):
        self.assertEqual(minimal_dirs(["A/B", "A/C"]), ["A/B", "A/C"])

    def test_example_from_spec(self):
        dirs = ["A/B", "A/B/C", "A/C/A", "A/C/B"]
        expected = ["A/B", "A/C/A", "A/C/B"]
        self.assertEqual(minimal_dirs(dirs), expected)

    def test_unsorted_input(self):
        dirs = ["A/B/C", "A/B"]
        expected = ["A/B"]
        self.assertEqual(minimal_dirs(dirs), expected)

    def test_multiple_nested_levels(self):
        dirs = ["A", "A/B", "A/B/C", "A/B/D", "E/F"]
        expected = ["A", "E/F"]
        self.assertEqual(minimal_dirs(dirs), expected)

    def test_duplicates(self):
        dirs = ["A/B", "A/B", "A/B/C"]
        expected = ["A/B"]
        self.assertEqual(minimal_dirs(dirs), expected)

if __name__ == "__main__":
    unittest.main()
