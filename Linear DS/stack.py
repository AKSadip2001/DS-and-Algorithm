class Stack:
    n = 100
    def __init__(self):
        self.stack = []

    def push(self, int):
        if(len(self.stack)==Stack.n):
            return print("Stack is full")
        self.stack.append(int)
        print(str(int) + " pushed to stack")

    def pop(self):
        if(len(self.stack)==0):
            return print("Nothing to pop")
        return self.stack.remove(self.stack[len(self.stack)-1])

    def printStack(self):
        if(len(self.stack)==0):
            return print("Stack is empty")
        for elem in self.stack:
            print(elem, end=" ")
        print()


stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.pop()

stack.printStack()