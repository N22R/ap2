import unittest
from src.sum import TreeNode, sum_of_depths

class TestSumOfDepths(unittest.TestCase):
    def test_empty_tree(self):
        self.assertEqual(sum_of_depths(None), 0)

    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(sum_of_depths(root), 0)

    def test_tree_example(self):
        root = TreeNode(1)
        root.left = TreeNode(2, TreeNode(4), TreeNode(5))
        root.right = TreeNode(3)
        self.assertEqual(sum_of_depths(root), 6)

if __name__ == "__main__":
    unittest.main()