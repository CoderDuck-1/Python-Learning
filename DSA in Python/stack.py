# stack can be implented in python using list
#Functions used:-
# 1- s.pop() - removes last element . underflow: cannot pop from empty list
# 2- s[-1] - when we dont want to delete the last entered element
# Comes with the problems of a list. Time complexity in copying

#So we implement it using collections.deque

from collections import deque
stack = deque()
print(dir(stack))
stack.append("a")
stack.append("b")
stack.append("c")
print(stack)
stack.pop()
print(stack)
print(stack.index("b"))

#Stack class using deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)