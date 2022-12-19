class Node:
    """
    Tree Node class containing one parameter.

    Attributes:
        value (int): Integer, data of this Node.
        left: Node Class, left child of this Node.
        right: Node Class, right Child of this Node.
    """

    def __init__(self, value):
        """
        Init of Node Class with 'value' parameter.

        :parameter int value: Data of this Node.
        """
        self.value = value
        self.left = None
        self.right = None

    def __iter__(self):
        """
        Generator of Node Class (Breadth-First Traversal Algorithm based).

        :return: Generator of Tree
        """
        order = []
        order = breadthFirstTraverse(self, order)
        yield order

    # Depth-First Traversal
    def preOrderTraverse(self, flag_order):
        """
        Pre-Order Traversal, one of the Depth-First Search Algorithm.

        :parameter list flag_order: empty integer list which user are going to store the pre-order traverse
        :return: flag_order: Integer List, list of node starting from first to last
                    based on pre-order Traverse
        """
        flag_order.append(self.value)
        if self.left:
            self.left.preOrderTraverse(flag_order)

        if self.right:
            self.right.preOrderTraverse(flag_order)

        return flag_order

    def inOrderTraverse(self, flag_order):
        """
        In-Order Traversal, one of the Depth-First Search Algorithm.

        :parameter list flag_order: empty integer list which user are going to store the in-order traverse
        :return: flag_order Integer List, list of node starting from first to last
                    based on in-order Traverse
        """
        if self.left:
            self.left.inOrderTraverse(flag_order)

        flag_order.append(self.value)

        if self.right:
            self.right.inOrderTraverse(flag_order)

        return flag_order

    def postOrderTraverse(self, flag_order):
        """
        Post-Order Traversal, one of the Depth-First Search Algorithm.

        :parameter list flag_order: empty integer list which user are going to store the post-order traverse
        :return: flag_order Integer List, list of node starting from first to last
                    based on post-order Traverse
        """
        if self.left:
            self.left.postOrderTraverse(flag_order)

        if self.right:
            self.right.postOrderTraverse(flag_order)
        flag_order.append(self.value)

        return flag_order


def nodeCount(root: Node) -> int:
    """
    Count a total number of nodes of the 'root' tree instance.

    :param Node root: Node Class, the Binary tree
    :return: Integer, total number of nodes in this Binary Tree
    """
    if root is None:
        return 0

    return nodeCount(root.left) + nodeCount(root.right) + 1


def treeHeight(node: Node):
    """
    Calculate the height of the tree (Starts from root)

    :param node: Node Class, the root node of the tree
    :return: Integer, height of the tree
    """
    if node is None:
        return 0
    else:
        # Compute the height of each subtree
        leftHeight = treeHeight(node.left)
        rightHeight = treeHeight(node.right)

        # Use the larger one
        if leftHeight > rightHeight:
            return leftHeight + 1
        else:
            return rightHeight + 1


def breadthFirstTraverse(root: Node, flag_order):
    flag_order.append(root.value)
    if root.left:
        flag_order.append(root.left.value)
    if root.right:
        flag_order.append(root.right.value)
    breadthFirstTraverse(root.left, flag_order)
    breadthFirstTraverse(root.right, flag_order)
    return flag_order
