class Stack():
    def __init__(self):
        self.list = []
    def __len__(self):
        return len(self.list)
    def __str__(self):
        return str(self.list)
    def push(self, item):
        self.list.append(item)
    def pop(self):
        return self.list.pop()    
    
class QueueStack:
    def __init__(self):
        self.inStack = Stack()
        self.outStack = Stack()
    def enqueue(self, item):
        self.inStack.push(item)
        
    def dequeue(self):
        if 