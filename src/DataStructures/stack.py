from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        self.container.pop()

    def isEmpty(self):
        return len(self.container) == 0

    def peek(self):
        return self.container[-1]

    def size(self):
        return len(self.container)


s = Stack()
s.push(97)
s.push(64)
s.push(84)
s.push(69)
s.push(84)
print(s.peek())
print(s.isEmpty())
print(s.size())
print(s.pop())
print(s.peek())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.isEmpty())
print(s.size())
