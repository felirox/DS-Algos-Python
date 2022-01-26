class Stack:
    def __init__(self,limit):
        self.maxSize=limit
        self.list=[]
    
    def __str__(self):
        if self.isEmptyy() is True:
            return "Stack is empty"
        else:
            values=[str(self.list[x-1]) for x in range(len(self.list),0,-1)]
            return '\n'.join(values)
        
    def isEmptyy(self):
        if self.list ==[]:
            return True
        else:
            return False
    
    def isFull(self):
        if len(self.list)==self.maxSize:
            return True
        else:
            return False
        
    def push(self,value):
        if self.isFull() is True:
            return "Full bro"
        else:
            self.list.append(value)
            return (value," added successfully")
    def pop(self):
        if self.isEmptyy() is True:
            return "Empty already bro, no pop"
        else:
            
            return (self.list.pop(), " removed successfully")
        
cs = Stack(2)

print(cs.isEmptyy())
print(cs.isFull())
print(cs.push(1))
print(cs.push(2))
print(cs.push(5))
print(cs.pop())
print(cs)
print(cs.pop())
print(cs)
print(cs.pop())
print(cs)
