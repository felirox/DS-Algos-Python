
class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None
        
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
 
    # def __iter__(self):
    #     cN = self.head
    #     while cN:
    #         yield cN
    #         cN= cN.next
            
class Queue:
    def __init__(self):
        self.linkedList = LinkedList()
               
    def __str__(self):
        val = [str(x.value) for x in self.linkedList]
        return ' '.join(val)
    
    def isEmpty(self):
        if self.linkedList.head == None:
            return True
        else:
            return False
    
    def enqueue(self,val):
        newNode = Node(val)
        if self.linkedList.head is None:
            self.linkedList.head = newNode
            self.linkedList.tail = newNode
        else:
            self.linkedList.tail.next = newNode
            self.linkedList.tail = newNode
        return val  
        
    def dequeue(self):
        if self.linkedList.head is None:
            return "Empty Queue"
        elif self.linkedList.head == self.linkedList.tail:
            tempp = self.linkedList.head.value
            self.linkedList.head = None
            self.linkedList.tail = None
            return tempp
            
        else:
            tempp = self.linkedList.head.value
            self.linkedList.head = self.linkedList.head.next
            return tempp
        
    def peek(self):
        if self.linkedList.head is None:
            return "Empty Queue"
        else:
            tempp = self.linkedList.head.value
            return tempp
        
    def deleteQ(self):
        if self.linkedList.head is None:
            return "Empty Queue"
        else:
            self.linkedList.head = None
            self.linkedList.tail = None
            return "Queue deleted successfully"
        
            
            
# nQ = Queue()
# print(nQ.enqueue(1))
# print(nQ.enqueue(2))
# print(nQ.enqueue(3))
# print(nQ)
# print(nQ.dequeue())
# print(nQ.dequeue())
# print(nQ.peek())
# print(nQ.deleteQ())
# print(nQ)