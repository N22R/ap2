class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def sum_of_depths(root: TreeNode) -> int:
    def calculate_depth(node, depth):
        if node is None:
            return 0
        return depth + calculate_depth(node.left, depth + 1) + calculate_depth(node.right, depth + 1)

    return calculate_depth(root, 0)