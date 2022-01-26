class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
    
class linkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        
    def __iter__ (self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode=curNode.next
        
        
class Stack:
    def __init__(self):
        self.linkedList=linkedList()
        
    def __str__(self):
        if self.isEmpty():
            return "Empty Stack"
        else:
            cal = [str(x.value) for x in self.linkedList]
            return '\n'.join(cal)
        
    def isEmpty(self):
        if self.linkedList.head==None:
            return True
        else:
            return False
        
    def push(self,value):
        node = Node(value)
        node.next=self.linkedList.head
        self.linkedList.head=node
        
    def pop(self):
        if self.isEmpty():
            return "Empty Stack"
        else:
            nV=self.linkedList.head.value
            self.linkedList.head = self.linkedList.head.next
            return nV
        
    def peek(self): #show the top element   
        if self.isEmpty():
            return "Empty Stack"
        else:
            nV=self.linkedList.head.value
            return nV
        
    def deleteL(self):
        self.linkedList.head=None
        
cStack = Stack()
print(cStack.isEmpty())
print(cStack.push(1))
print(cStack.push(2))
print(cStack.push(3))
print(cStack.push(4))
print(cStack)
print("0----")
print(cStack.pop())
print(cStack.peek())