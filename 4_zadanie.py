class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.count = 0

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.count = self.count + 1

    def pop(self):
        if self.top == None:
            raise IndexError("pop from empty stack")
        node = self.top
        self.top = node.next
        self.count = self.count - 1
        return node.value

    def peek(self):
        if self.top == None:
            raise IndexError("peek from empty stack")
        return self.top.value

    def is_empty(self):
        if self.top == None:
            return True
        else:
            return False


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.peek())
print(stack.pop())
print(stack.pop())
print(stack.is_empty())
print(stack.pop())
print(stack.is_empty())
