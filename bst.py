from btree import *
from mergeSort import *

'''Algorithm Answer is below'''


def arrayToBST(arr, root: Node):
    """
    Create Binary Search Tree based on the order of the array.

    :parameter list arr: List, Array consisted of node data.
    :parameter Node root: Node Class, Node which is going to be converted according to arr variable.
    :return: None Object, if and only if the root variable is None (tree is empty)
    """
    # Base Case
    if root is None:
        return

    # First update the left subtree
    arrayToBST(arr, root.left)

    # Update root's data delete the value from array
    root.value = arr[0]
    arr.pop(0)

    # Update the right subtree
    arrayToBST(arr, root.right)


def binaryTreeToBST(root):
    """
    Binary Tree to Binary Search Tree Function

    :param Node root: Node Class, root node of the Binary Tree
    """
    if root is None:
        print("This is an empty Tree.")
        return

    temp_array = []

    temp_array = root.inOrderTraverse(temp_array)

    mergeSort(temp_array)

    arrayToBST(temp_array, root)




