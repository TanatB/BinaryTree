from btree import *

'''Algorithm Answer is below'''


def invertTree(root: Node):
    """
    Invert the input tree around its vertical axis.

    :param Node root: Node Class
    :return: None Object, if and only if the tree is empty. None if function runs successful too
            (Due to the function is a setter function)
    """
    if root is None:
        return
    else:
        invertTree(root.left)

        invertTree(root.right)

        temp_node = root.left
        root.left = root.right
        root.right = temp_node


