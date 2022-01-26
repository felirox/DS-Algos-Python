class Stack:
    def __init__(self):
        self.list=[]
    
    def __str__(self):
        if self.isEmptyy() is True:
            return "Stack is empty"
        else:
            values=[str(self.list[x-1]) for x in range(len(self.list),0,-1)]
            return '\n'.join(values)
    
    def isEmptyy(self):
        if self.list == []:
            return True
        else:
            return  False
        
    def push(self,value):
        self.list.append(value)
        return (value," added successfully")
        
    def pop (self):
        if self.isEmptyy() is True:
            return "Stack is empty"
        else:
            return( self.list.pop(), " removed successfully")
        
    def peek(self):
        if self.isEmptyy() is True:
            return "Stack is empty"
        else:
            return self.list[-1]
        
    def deleteL(self):
        self.list=[]
        
custS = Stack()
print(custS.isEmptyy())
print(custS.pop())
print(custS.push(1))
print(custS.push(10))
print(custS.push(23))
print(custS)
print(custS)
print(custS)
print(custS.pop())
print(custS)
print(custS.peek())
print(custS.deleteL())
print(custS.isEmptyy())