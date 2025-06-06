import unittest
from src.kruskal import kruskal, UnionFind

class TestKruskalAlgorithm(unittest.TestCase):
    def test_basic_tree(self):
        edges = [(1, 0, 1), (3, 1, 2), (2, 0, 2)]
        n = 3
        self.assertEqual(kruskal(edges, n), 3)  # Мінімальне остовне дерево

    def test_disconnected_graph(self):
        edges = [(5, 0, 1), (2, 2, 3)]
        n = 4
        self.assertEqual(kruskal(edges, n), 7)  # Граф не пов'язаний повністю

    def test_large_graph(self):
        edges = [(1, 0, 1), (1, 1, 2), (1, 2, 3), (1, 3, 4), (1, 4, 0)]
        n = 5
        self.assertEqual(kruskal(edges, n), 4)

    def test_single_node(self):
        edges = []
        n = 1
        self.assertEqual(kruskal(edges, n), 0)  # Граф з одним вузлом не має ребер

    def test_no_edges(self):
        edges = []
        n = 5
        self.assertEqual(kruskal(edges, n), 0)  # Граф без ребер

if __name__ == "__main__":
    unittest.main()