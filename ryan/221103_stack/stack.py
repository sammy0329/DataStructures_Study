class Stack:
    def __init__(self):
        self.stack = []

    def get_size(self):
        return len(self.stack)

    def pop(self):
        if self.get_size() == 0:
            return -1

        else:
            return self.stack.pop()

    def push(self, value: int):
        self.stack.append(value)

    def top(self):
        if self.get_size() == 0:
            return -1

        else:
            return self.stack[-1]
