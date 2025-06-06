import unittest
from src.findP import find_3nums

class TestFind3Nums(unittest.TestCase):
    def test_example_case(self):
        nums = [1, 2, 3]
        num_P = 6
        expected_output = "Такі числа є"
        self.assertEqual(find_3nums(nums, num_P), expected_output)

    def test_no_matching_numbers(self):
        nums = [1, 2, 4]
        num_P = 10
        expected_output = "Таких чисел немає"
        self.assertEqual(find_3nums(nums, num_P), expected_output)

    def test_duplicate_numbers(self):
        nums = [1, 2, 2, 3, 3]
        num_P = 6
        expected_output = "Такі числа є"
        self.assertEqual(find_3nums(nums, num_P), expected_output)

if __name__ == "__main__":
    unittest.main()