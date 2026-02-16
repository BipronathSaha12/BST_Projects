import unittest
from bst.tree import BinarySearchTree

class TestBST(unittest.TestCase):

    def setUp(self):
        self.bst = BinarySearchTree()
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(20)

    def test_insert(self):
        self.assertEqual(self.bst.inorder(), [5, 10, 20])

    def test_search(self):
        self.assertIsNotNone(self.bst.search(10))
        self.assertIsNone(self.bst.search(99))

    def test_height(self):
        self.assertEqual(self.bst.height(), 1)

if __name__ == "__main__":
    unittest.main()
