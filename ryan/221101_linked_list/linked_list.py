class Node:
    def __init__(self, value, front, back):
        self.value = value
        self.front = front
        self.back = back


class LinkedList:
    def __init__(self):
        self.root = Node(None, None, None)

    @staticmethod
    def get_front(node: Node):
        if node.front is not None:
            return node.front

        else:
            return node

    @staticmethod
    def get_back(node: Node):
        if node.back is not None:
            return node.back

        else:
            return node

    @staticmethod
    def self_destruction(node: Node):
        if node.front is not None:
            front_ = node.front
            back_ = node.back

            front_.back = back_
            if back_ is not None:
                back_.front = front_

            return front_

        else:
            return node

    @staticmethod
    def insert(node: Node, new_word: str):
        back_ = node.back
        new = Node(new_word, node, back_)
        node.back = new

        if back_ is not None:
            back_.front = new

        return new
