import unittest
from src.rabin_karp import rabin_karp

class TestRabinKarp(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(rabin_karp("abcdefabcdef", "abc"), [0, 6])
        self.assertEqual(rabin_karp("aaaaa", "aa"), [0, 1, 2, 3])
        self.assertEqual(rabin_karp("hello world", "world"), [6])

    def test_no_match(self):
        self.assertEqual(rabin_karp("abcdef", "xyz"), [])
        self.assertEqual(rabin_karp("", "a"), [])

    def test_edge_cases(self):
        self.assertEqual(rabin_karp("a", "a"), [0])
        self.assertEqual(rabin_karp("abc", ""), [])
        self.assertEqual(rabin_karp("", ""), [])

if __name__ == "__main__":
    unittest.main()