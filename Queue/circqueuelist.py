class QueueClass:
    def __init__(self, maxSize):
        self.items=maxSize *[None]
        self.maxSize=maxSize
        self.start = -1
        self.top = -1
        
    def __str__(self):
        vall = [str(x) for x in self.items]
        return ' '.join(vall)
    
    def isFull(self):
        if self.top + 1 == self.start: #when not pointing to 0
            return True
        elif self.start == 0 and self.top + 1 ==self.maxSize: #when pointing to 0
            return True
        else:
            return False
    
    def isEmpty(self):
        if self.start == -1 and self.top ==-1:
            return True
        else:
            return False
        
    def enque(self,val):
        if self.isFull():
            return "Queue is full"
        else:
            if self.top+1 == self.maxSize:
                self.top =0
            else:
                self.top +=1
                if self.start == -1:
                    self.start =0
            self.items[self.top]=val
            return "Element added successfully"
        
    def deque(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            fS=self.items[self.start]
            start = self.start
            if self.top == self.start:
                self.top ==-1
                self.start == -1
            elif self.start +1 == self.maxSize:
                self.start =0
            else:
                self.start +=1
            self.items[start]=None
            return (fS," removed successfully")
        
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            return self.items[self.start]
        
    def delete(self):
        self.start = -1
        self.top = -1
        self.items = [None]*self.maxSize
        return "Queue deleted successfully"
                
                
        
            
cQ = QueueClass(5)
print(cQ.isFull())
print(cQ.isEmpty())
print(cQ.enque(1))
print(cQ.enque(2))
print(cQ.enque(3))
print(cQ) 
print(cQ.deque())
print(cQ)    
print(cQ.peek())
print(cQ.delete())
print(cQ.isEmpty())
print(cQ)  