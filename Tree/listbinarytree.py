from sys import maxsize


class BTclass:
    def __init__(self,size):
        self.customList=size*[None]
        self.lastUsedIndex=0
        self.maxSize=size
        
    def insertNode(self,value):
        if self.lastUsedIndex+1 == self.maxSize:
            return "BT is Full"
        else:
            self.customList[self.lastUsedIndex+1]=value
            self.lastUsedIndex+=1
            return "Node inserted successfully"
    
        
BT = BTclass(10)
print(BT.insertNode(1))


