class Node:
    def __init__(self,value=None, next=None):
        self.value = value
        self.next = next
        
    def __str__(self):
        string=str(self.value)
        if self.next: #IF next value exists for the node, then the next value is also printed along with the node val
            string+=','+str(self.next)
        return string
    
class Stack:
    def __init__(self):
        self.top=None
        self.minNode=None
    
    def min(self):
        if not self.minNode:
            return None
        else:
            return self.minNode.value
        
    def push(self,val):
        if self.minNode and (self.minNode.value<val):
            self.minNode = Node(value = self.minNode.value, next=self.minNode)
        else:
            self.minNode = Node(value = val, next = self.minNode)
            
        self.top = Node(value = val, next = self.top)
        
    def pop(self):
        if self.top is None:
            return "Empty Stack"
        else:
            self.minNode =self.minNode.next
            item = self.top.value
            self.top = self.top.next
            return item
        
cS = Stack()
cS.push(5)
print(cS.min())
cS.push(6)
print(cS.min())
cS.push(3)
print(cS.min())
cS.push(1)
print(cS.min())
cS.pop()
print(cS.min())
cS.pop()
print(cS.min())
cS.pop()
print(cS.min())
cS.pop()
print(cS.min())


            