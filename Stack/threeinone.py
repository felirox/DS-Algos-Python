class MultiStack:
    def __init__(self,stackSize):
        self.numberStacks=3
        self.cusList = [None]*(stackSize*self.numberStacks)
        self.sizes = [0]*self.numberStacks
        self.stackSize = stackSize
        
    def isFull(self, sNum):
        if self.sizes[sNum]==self.stackSize:
            return True
        else:
            return False
        
    def isEmpty(self, sNum):
        if self.sizes[sNum]==0:
            return True
        else:
            return False
        
    def indexOfTop(self,sNum):
        offset = sNum * self.stackSize
        return offset + self.sizes[sNum]-1
    
    def push(self, sNum, val):
        if self.isFull(sNum):
            return "Stack is full"
        else:
            self.sizes[sNum] +=1
            self.cusList[self.indexOfTop(sNum)] = val
        
        return "Element added successfully"
    
    def pop (self, sNum):
        if self.isEmpty(sNum):
            return "Stack is empty"
        else:
            rval = self.cusList[self.indexOfTop(sNum)]
            self.cusList[self.indexOfTop(sNum)] = None
            self.sizes[sNum]-=1
            return rval
    
    def peek (self, sNum):
        if self.isEmpty(sNum):
            return "Stack is empty"
        else:
            rval = self.cusList[self.indexOfTop(sNum)]
            return rval
            
            
cStack = MultiStack(9)
print(cStack.isFull(1))
print(cStack.isEmpty(2))
cStack.push(1,1)
cStack.push(2,4)
cStack.push(0,2)
cStack.push(1,7)
print(cStack.peek(2))
       
    
    