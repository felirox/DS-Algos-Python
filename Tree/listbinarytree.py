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
    
    def searchNode(self,value):
        if value in self.customList:
            return "Found"
        return "Not Found"
    
    def preTrav(self, index=1):
        
        if index>self.lastUsedIndex:
            return 
        else:
            print(self.customList[index])
            self.preTrav(index*2) #left child
            self.preTrav(index*2 + 1) #right child
            
    def inTrav(self,index=1):
        if index>self.lastUsedIndex:
            return
        else:
            self.inTrav(index*2)
            print(self.customList[index])
            self.inTrav(index*2 +1)
    
    def postTrav(self,index=1):
        if index>self.lastUsedIndex:
            return
        else:
            self.postTrav(index*2)
            self.postTrav(index*2 +1)
            print(self.customList[index])
            
    def levelTrav(self, index=1):
        for i in range(index,self.lastUsedIndex+1):
            
            print(self.customList[i])
            
            
        
BT = BTclass(10)
print(BT.insertNode("Drinks"))
print(BT.insertNode("Hot"))
print(BT.insertNode("Cold"))
print(BT.insertNode("Tea"))
print(BT.insertNode("Coffee"))
print(BT.searchNode("Coldd"))
BT.levelTrav()



