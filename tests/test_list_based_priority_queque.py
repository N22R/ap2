import unittest
from src.list_based_priority_queue import PriorityQueue

class TestPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.queue = PriorityQueue()

    def test_insert_and_peek(self):
        self.queue.insert("Task 1", 2)
        self.queue.insert("Task 2", 3)
        self.queue.insert("Task 3", 1)
        self.assertEqual(self.queue.peek(), [("Task 2", 3), ("Task 1", 2), ("Task 3", 1)])

    def test_remove(self):
        self.queue.insert("Task 1", 2)
        self.queue.insert("Task 2", 3)
        self.queue.insert("Task 3", 1)
        self.assertEqual(self.queue.remove(), "Task 2")
        self.assertEqual(self.queue.peek(), [("Task 1", 2), ("Task 3", 1)])

    def test_remove_empty_queue(self):
        self.assertIsNone(self.queue.remove())

    def test_peek_empty_queue(self):
        self.assertEqual(self.queue.peek(), [])

if __name__ == "__main__":
    unittest.main()