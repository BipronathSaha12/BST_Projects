from .node import Node


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # INSERT
    def insert(self, key: int):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self._insert(root.left, key)
        elif key > root.key:
            root.right = self._insert(root.right, key)
        return root

    # SEARCH
    def search(self, key: int):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._search(root.left, key)
        return self._search(root.right, key)

    # DELETE
    def delete(self, key: int):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return None

        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            temp = self._min_value(root.right)
            root.key = temp.key
            root.right = self._delete(root.right, temp.key)

        return root

    def _min_value(self, node):
        while node.left:
            node = node.left
        return node

    # TRAVERSALS
    def inorder(self):
        return self._inorder(self.root)

    def _inorder(self, root):
        if not root:
            return []
        return self._inorder(root.left) + [root.key] + self._inorder(root.right)

    def preorder(self):
        return self._preorder(self.root)

    def _preorder(self, root):
        if not root:
            return []
        return [root.key] + self._preorder(root.left) + self._preorder(root.right)

    def postorder(self):
        return self._postorder(self.root)

    def _postorder(self, root):
        if not root:
            return []
        return self._postorder(root.left) + self._postorder(root.right) + [root.key]

    # HEIGHT
    def height(self):
        return self._height(self.root)

    def _height(self, root):
        if not root:
            return -1
        return 1 + max(self._height(root.left), self._height(root.right))

    # BALANCE
    def is_balanced(self):
        return self._balance_check(self.root) != -1

    def _balance_check(self, root):
        if not root:
            return 0
        left = self._balance_check(root.left)
        right = self._balance_check(root.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return 1 + max(left, right)
