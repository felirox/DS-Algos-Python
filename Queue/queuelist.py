class Queue:
    def __init__(self):
        self.items=[]
    
    def __str__(self):
        val=[str(x) for x in self.items]
        return ' '.join(val)
    
    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False
        
    def enqueue (self,val):
        self.items.append(val) #amotizes constant - bad time complexity - On2
        return "Element added successfully"
        
    def dequeue(self):
        if self.items == []:
            return "Empty Queue"
        else:
            return (str(self.items.pop(0)) + " removed successfully")
        #takes O(n) coz all elements needs to shift one before the first element
        
    def peek(self):    
        if self.items == []:
            return "Empty Queue"
        else:
            return self.items[0]
        
    def deleteQ(self):
        self.items= None
    
cQue = Queue()
print(cQue.isEmpty())
print(cQue.enqueue(1))
print(cQue.enqueue(4))
print(cQue.enqueue(15))
print(cQue)
print(cQue.dequeue())