from btree import *

'''Algorithm Answer is below'''


def isSymmetricalTree(root: Node) -> bool:
    """
    Operates with isMirror() checking if the input tree is symmetrical around its vertical axis.

    :parameter Node root: Node Class, root of the tree which are going to be checked
    :return: Boolean, True if root variable is symmetrical. Return False otherwise
    """
    if root is None:
        return True
    else:
        return isMirror(root.left, root.right)


def isMirror(left: Node, right: Node) -> bool:
    """
    Helper Function Determining the Sub-Tree whether it is a Mirror tree or not

    Firstly, checking if the tree has only a root node. If so, return True. Then,
    dividing big tree into two subtree, and operating a comparison. Lastly, creating
    an inner pairs of left and right subtree and also outer pairs of left and right
    subtree.

    :param Node left: left subtree Node
    :param Node right: right subtree Node
    :return: Boolean, True if the tree is symmetric, False otherwise
    """
    if left is None and right is None:
        return True
    if left is None or right is None:
        return False
    if left.value == right.value:
        # Left of left subtree vs. Right of right subtree
        innerPair = isMirror(left.left, right.right)

        # Right of left subtree vs. Left of right subtree
        outerPair = isMirror(left.right, right.left)

        return innerPair and outerPair
    else:
        return False
