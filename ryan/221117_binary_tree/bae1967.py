import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, node_id=None):
        self.node_id = node_id
        self.weight = 0
        self.childs = {}

    def set_child(self, child_node, weight):
        self.childs[child_node] = weight


class BinaryTree:
    def __init__(self):
        self.nodes = []
        self.child_max = 0

    def initial_tree(self):
        num_input = int(input())
        self.nodes = [Node(idx) for idx in range(num_input)]

        for _ in range(num_input - 1):
            node_id, child_id, weight = list(map(int, sys.stdin.readline().strip().split()))
            node_id -= 1
            child_id -= 1

            child_node = self.nodes[child_id]

            self.nodes[node_id].set_child(child_node, weight)

    def postorder(self, node=None):
        node = node if node is not None else self.nodes[0]
        each_weight_list = []

        if len(node.childs) == 0:
            node.weight = 0
            return node.weight

        for n in node.childs.keys():
            self.postorder(n)

        for n in node.childs.keys():
            each_weight = node.childs[n] + n.weight
            each_weight_list.append(each_weight)

        node.weight = max(each_weight_list)

        if len(node.childs) >= 2:
            each_weight_list.remove(node.weight)
            self.child_max = max(node.weight + max(each_weight_list), self.child_max)

        else:
            self.child_max = max(node.weight, self.child_max)

        return node.weight


tree = BinaryTree()
tree.initial_tree()
tree.postorder()

print(tree.child_max)
