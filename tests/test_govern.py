import unittest
from collections import defaultdict
from src.govern import  sort

class TestDocumentSorting(unittest.TestCase):

    def setUp(self):
        self.input_data = [
            ("visa", "foreignpassport"),
            ("visa", "hotel"),
            ("visa", "bankstatement"),
            ("bankstatement", "nationalpassport"),
            ("hotel", "creditcard"),
            ("creditcard", "nationalpassport"),
            ("nationalpassport", "birthcertificate"),
            ("foreignpassport", "nationalpassport"),
            ("foreignpassport", "militarycertificate"),
        ]

        self.dependencies = defaultdict(list)
        self.in_degree = defaultdict(int)

        for doc, required_doc in self.input_data:
            self.dependencies[required_doc].append(doc)
            self.in_degree[doc] += 1
            if required_doc not in self.in_degree:
                self.in_degree[required_doc] = 0

    def test_sort_documents(self):
        sorted_docs = sort(self.dependencies, self.in_degree)
        doc_positions = {doc: i for i, doc in enumerate(sorted_docs)}


if __name__ == "__main__":
    unittest.main()