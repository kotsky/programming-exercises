
class Stack:
    def __init__(self):
        self.stack = []
        self.min = []
        self.max = []

    def peek(self):
        return self.stack[-1] if len(self.stack) > 0 else None
    
    def pop(self):
        self.min.pop()
        self.max.pop()
        return self.stack.pop() if len(self.stack) > 0 else None
    
    def push(self, number):
        if len(self.stack) > 0:
            self.max.append(max(number, self.max[-1]))
            self.min.append(min(number, self.min[-1]))
        else:
            self.max.append(number)
            self.min.append(number)
        self.stack.append(number)
    
    def getMin(self):
        return self.min[-1] if len(self.stack) > 0 else None
    
    def getMax(self):
        return self.max[-1] if len(self.stack) > 0 else None
