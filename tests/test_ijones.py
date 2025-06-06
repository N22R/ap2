import unittest
from src.ijones import find_all_paths

class TestIJones(unittest.TestCase):
    def test_example_1(self):
        grid = [
            ['a', 'a', 'a'],
            ['c', 'a', 'b'],
            ['d', 'e', 'f']
        ]
        expected_paths = 5
        self.assertEqual(find_all_paths(grid), expected_paths)

    def test_example_2(self):
        grid = [
            ['a', 'b', 'c', 'd', 'e', 'f', 'a', 'g', 'h', 'i']
        ]
        expected_paths = 2
        self.assertEqual(find_all_paths(grid), expected_paths)

    def test_example_3(self):
        grid = [
            ['a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['a', 'a', 'a', 'a', 'a', 'a', 'a'],
            ['a', 'a', 'a', 'a', 'a', 'a', 'a']
        ]
        expected_paths = 201684
        self.assertEqual(find_all_paths(grid), expected_paths)

    def test_example_5(self):
        grid = [
            ['a', 'a', 'b', 'a'],
            ['c', 'a', 'b', 'p'],
            ['d', 'e', 'f', 'a']
        ]
        expected_paths = 10
        self.assertEqual(find_all_paths(grid), expected_paths)

if __name__ == '__main__':
    unittest.main()