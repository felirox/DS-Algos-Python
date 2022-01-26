class PlateStack:
    def __init__(self,capacity):
        self.capacity = capacity
        self.stacks=[]
        
    def __str__(self):
        return self.stacks

    def __iter__(self):
        return self.stacks
    
    def push(self,item):
        if len(self.stacks)>0 and (len(self.stacks[-1]) <self.capacity):
            self.stacks[-1].append(item) #i1
        else:
            self.stacks.append([item]) #i2
    
    def pop(self):
        while len(self.stacks) and len(self.stacks[-1])==0:
            self.stacks.pop() #i3
        if len(self.stacks)==0:
            return None
        else:
            return self.stacks[-1].pop() # i4
        
    def popAt(self,stackNo):
        if len(self.stacks[stackNo])>0:
            return self.stacks[stackNo].pop()
        else:
            return None
    def printAll(self):
        for stack in self.stacks:
            print(stack)
        

cS = PlateStack(3)

cS.push(2)
cS.push(4)
cS.push(82)
cS.push(12)
cS.push(5)

print(cS.pop())
cS.printAll()

print(cS.pop())
cS.printAll()

print(cS.pop())
cS.printAll()

print(cS.pop())
cS.printAll()

print(cS.pop())
cS.printAll()

print(cS.pop())
cS.printAll()
