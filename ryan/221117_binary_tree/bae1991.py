class Node:
    def __init__(self, node_id=None, left=None, right=None):
        self.node_id = node_id
        self.left = None
        self.right = None

    def set_lr(self, left, right):
        self.left = left
        self.right = right

    def visit(self):
        print(chr(self.node_id + 65), end='')


class BinaryTree:
    def __init__(self):
        self.nodes = [Node(idx) for idx in range(26)]

    def initial_tree(self):
        num_input = int(input())
        for _ in range(num_input):
            node_id, left, right = list(map(ord, input().split()))

            node_id -= 65
            left_node = self.nodes[left-65] if left >= 65 else None
            right_node = self.nodes[right-65] if right >= 65 else None

            self.nodes[node_id].set_lr(left_node, right_node)

    def preorder(self, node=None):
        node = node if node is not None else self.nodes[0]
        node.visit()

        if node.left is not None:
            self.preorder(node.left)

        if node.right is not None:
            self.preorder(node.right)

        if node.left is None and node.right is None:
            return

    def postorder(self, node=None):
        node = node if node is not None else self.nodes[0]
        if node.left is not None:
            self.postorder(node.left)

        if node.right is not None:
            self.postorder(node.right)

        node.visit()

        if node.left is None and node.right is None:
            return

    def inorder(self, node=None):
        node = node if node is not None else self.nodes[0]
        if node.left is not None:
            self.inorder(node.left)

        node.visit()

        if node.right is not None:
            self.inorder(node.right)

        if node.left is None and node.right is None:
            return


tree = BinaryTree()
tree.initial_tree()
tree.preorder()
print()
tree.inorder()
print()
tree.postorder()
