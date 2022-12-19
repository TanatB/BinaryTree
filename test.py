import unittest
from btree import *
from bst import *
from inversion import *
from symmetree import *


class TestBtree(unittest.TestCase):

    def setUp(self):
        self.root_test1 = Node(4)
        self.root_test1.left = Node(2)
        self.root_test1.right = Node(6)
        self.root_test1.left.left = Node(1)
        self.root_test1.left.right = Node(3)
        self.root_test1.right.left = Node(5)
        self.root_test1.right.right = Node(7)
        '''
                     4
                   /   \
                  2     6
                 / \   / \
                1   3 5   7
        '''

        self.root_test2 = Node(3)
        self.root_test2.left = Node(5)
        self.root_test2.left.left = Node(1)
        self.root_test2.left.left.left = Node(4)
        self.root_test2.left.left.left.left = Node(7)
        self.root_test2.left.left.left.left.left = Node(6)
        self.root_test2.left.left.left.left.left.left = Node(2)

        self.root_test3 = Node(6)
        self.root_test3.right = Node(5)
        self.root_test3.right.right = Node(1)
        self.root_test3.right.right.right = Node(4)
        self.root_test3.right.right.right.right = Node(7)
        self.root_test3.right.right.right.right.right = Node(3)
        self.root_test3.right.right.right.right.right.right = Node(2)

    def tearDown(self):
        pass

    def test_breadthFirst(self):
        order = []
        order = breadthFirstTraverse(self.root_test1, order)
        self.assertEqual(order, [4, 2, 6, 1, 3, 5, 7])

    def test_iter(self):
        pass

    def test_preOrder(self):
        preorder1, preorder2, preorder3 = [], [], []
        preorder1 = self.root_test1.preOrderTraverse(preorder1)
        preorder2 = self.root_test2.preOrderTraverse(preorder2)
        preorder3 = self.root_test3.preOrderTraverse(preorder3)

        # Edge case one: Balanced BST
        self.assertEqual(preorder1, [4, 2, 1, 3, 6, 5, 7])

        # Edge case two: Left skewed BST
        self.assertEqual(preorder2, [3, 5, 1, 4, 7, 6, 2])

        # Edge case three: Right skewed BST
        self.assertEqual(preorder3, [6, 5, 1, 4, 7, 3, 2])

    def test_inOrder(self):
        inorder1, inorder2, inorder3 = [], [], []
        inorder1 = self.root_test1.inOrderTraverse(inorder1)
        inorder2 = self.root_test2.inOrderTraverse(inorder2)
        inorder3 = self.root_test3.inOrderTraverse(inorder3)

        # Edge case one: Balanced BST
        self.assertEqual(inorder1, [1, 2, 3, 4, 5, 6, 7])

        # Edge case two: Left skewed BST
        self.assertEqual(inorder2, [2, 6, 7, 4, 1, 5, 3])

        # Edge case three: Right skewed BST
        self.assertEqual(inorder3, [6, 5, 1, 4, 7, 3, 2])

    def test_postOrder(self):
        self.assertEqual(self.root_test1.postOrderTraverse(), [1, 3, 2, 9, 6, 5, 4])

    def test_nodeCount(self):
        self.assertEqual(nodeCount(self.root_test1), 7)
        self.assertEqual(nodeCount(self.root_test2), 7)
        self.assertEqual(nodeCount(self.root_test3), 7)

    def test_treeHeight(self):
        self.assertEqual(treeHeight(self.root_test1), 3)
        self.assertEqual(treeHeight(self.root_test2), 7)
        self.assertEqual(treeHeight(self.root_test3), 7)


class TestBST(unittest.TestCase):

    def setUp(self):
        self.root_test4 = Node(1)
        self.root_test4.left = Node(2)
        self.root_test4.right = Node(5)
        self.root_test4.left.left = Node(3)
        self.root_test4.left.right = Node(4)
        self.root_test4.right.left = Node(6)
        self.root_test4.right.right = Node(7)
        ''' 
                  1
                /   \
               2     5
              / \   / \
             3   4 6   7
        '''

    def tearDown(self):
        pass

    def test_BTtoBST(self):
        inorder = []
        binaryTreeToBST(self.root_test4)
        self.assertEqual(self.root_test4.inOrderTraverse(inorder), [1, 2, 3, 4, 5, 6, 7])


class TestInversion(unittest.TestCase):

    def setUp(self):
        self.root_test7 = Node(1)
        self.root_test7.left = Node(2)
        self.root_test7.right = Node(5)
        self.root_test7.left.left = Node(3)
        self.root_test7.left.right = Node(4)
        self.root_test7.right.left = Node(6)
        self.root_test7.right.right = Node(7)
        ''' 
                          1
                        /   \
                       2     5
                      / \   / \
                     3   4 6   7
        '''

    def tearDown(self):
        pass

    def test_inversion(self):
        invertTree(self.root_test7)
        inorder = []
        inorder = self.root_test7.inOrderTraverse(inorder)
        self.assertEqual(inorder, [7, 5, 6, 1, 4, 2, 3])


class TestSymmetricalTree(unittest.TestCase):
    def setUp(self):
        self.root_test10 = Node(1)
        self.root_test10.left = Node(2)
        self.root_test10.right = Node(2)
        self.root_test10.left.left = Node(3)
        self.root_test10.left.right = Node(4)
        self.root_test10.right.left = Node(4)
        self.root_test10.right.right = Node(3)
        ''' 
                          1
                        /   \
                       2     2
                      / \   / \
                     3   4 4   3
        '''

    def tearDown(self):
        pass

    def test_symmetrical_tree(self):
        self.assertEqual(isSymmetricalTree(self.root_test10), True)


if __name__ == '__main__':
    unittest.main()
