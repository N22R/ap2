import unittest
from src.Breadth_First_Search import  matrix_to_graph, bfs_shortest_path

class TestMaze(unittest.TestCase):
    def setUp(self):
        self.matrix = [
            [1, 1, 0, 1],
            [0, 1, 1, 1],
            [1, 0, 1, 0],
            [1, 1, 1, 1]
        ]
        self.graph = matrix_to_graph(self.matrix)
        self.start = (0, 0)
        self.end = (3, 3)

    def test_matrix_to_graph(self):
        expected_keys = {(0, 0), (0, 1), (0, 3), (1, 1), (1, 2), (1, 3), (2, 0), (2, 2), (3, 0), (3, 1), (3, 2), (3, 3)}
        self.assertEqual(set(self.graph.keys()), expected_keys)

    def test_bfs_shortest_path_exists(self):
        self.assertEqual(bfs_shortest_path(self.graph, self.start, self.end), 6)

    def test_bfs_shortest_path_no_path(self):
        unreachable_start = (0, 2)
        self.assertEqual(bfs_shortest_path(self.graph, unreachable_start, self.end), -1)

if __name__ == "__main__":
    unittest.main()