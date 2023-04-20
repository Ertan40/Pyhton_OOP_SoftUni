class Stack:

    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        if self.data:
            return False
        return True

    def __str__(self):
        return f"[{', '.join(self.data[::-1])}]"


stack = Stack()
stack.push("apple")
stack.push("carrot")
print(str(stack)) #'[carrot, apple]')
print(stack.pop()) #'carrot'
print(stack.top()) #'apple')
stack.push("cucumber")
print(str(stack)) #'[cucumber, apple]')
print(stack.is_empty()) #, False)