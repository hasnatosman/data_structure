class Stack:
    def __init__(self, limit=10):
        self.stack = []
        self.limit = limit

    # for printing the stack contents
    def __str__(self):
        return ' '.join([str(i) for i in self.stack])

    # for pushing an element on the stack
    def push(self, data):
        if len(self.stack) >= self.limit:
            print('Stack overflow.')
        else:
            self.stack.append(data)

    # for popping the upper most data
    def pop(self):
        if len(self.stack) <= 0:
            return -1
        else:
            return self.stack.pop()

    # for peaking the top one data
    def peak(self):
        if len(self.stack) <= 0:
            return -1
        else:
            return self.stack[len(self.stack) - 1]

    # checking the stack empty or not.
    def is_empty(self):
        return self.stack == []

    # find the stack size
    def size(self):
        return len(self.stack)


if __name__ == '__main__':
    myStack = Stack()
    for i in range(10):
        myStack.push(i)
    print(myStack)
    myStack.pop()
    print(myStack)
    myStack.is_empty()
    print(myStack)
    myStack.peak()
    print(myStack.peak())
    myStack.size()
    print(myStack.size())
    print(myStack.is_empty())
