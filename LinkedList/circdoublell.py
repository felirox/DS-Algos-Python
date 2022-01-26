
class Node:
    def __init__(self,value=None):
        self.value = value
        self.next=None
        self.prev=None
        
class CirDLL:
    def __init__(self):
        self.head=None
        self.tail=None
        
    def __iter__(self):
        node=self.head
        while node:
            yield node
            
            if node.next ==self.tail.next: #why not self.head - self.tail.next apparently was used later
                break
            node = node.next
            
    def CreateCDLL(self, value):
        newNode=Node(value)
        self.head = newNode
        self.tail = newNode
        newNode.prev=newNode
        newNode.next=newNode
        return "CDLL created successfully"
    
    def insertCDLL (self,nodeValue,loc:int):
        if self.head is None:
            return "CDLL not existing"
        else:
            newNode=Node(nodeValue)
            if loc==0:
                newNode.next=self.head
                newNode.prev=self.head.prev
                self.head.prev=newNode
                self.head=newNode
                self.tail.next=newNode
            
            elif loc == -1:
                newNode.next=self.tail.next
                newNode.prev=self.tail
                self.head.prev=newNode
                self.tail.next=newNode
                self.tail=newNode
            else:
                tnode = self.head
                index=0
                while index<loc-1:
                    tnode=tnode.next
                    index+=1
                nextnode=tnode.next
                newNode.next=nextnode
                newNode.prev=tnode
                tnode.next=newNode
                nextnode.prev=newNode
            return "Inserted successfully in CDLL"
                
    def travCDLL(self):
        if self.head is None:
            return "CDLL not existing"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == None or str(tempNode.value) == "None":
                    print ("gungrrooooo")
                print(tempNode.value)
                if tempNode == self.tail:
                    break
                
                tempNode = tempNode.next
                
    def revTravCDLL(self):
        if self.head is None:
            return "CDLL not existing"
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                if tempNode == self.head:
                    break
                tempNode = tempNode.prev
                
    def searchCDLL(self,value):
        if self.head is None:
            return "CDLL not existing"
        else:
            tempNode = self.head
            i=0
            while tempNode:
                if tempNode == self.tail:
                    break
                if tempNode.value == value:
                    print("value found at position",i)
                i+=1
                tempNode = tempNode.next
                
    def delCDLL(self,index):
        if self.head is None:
            return "CDLL not existing"
        else:
            if index ==0:
                if self.head == self.tail:
                    self.head.next=None
                    self.head.prev = None
                    self.head = None
                    self.tail = None
                else:
                    
                    ttt = self.head
                    self.head = self.head.next
                    ttt.next = None
                    self.head.prev=self.tail
                    self.tail.next=self.head
            elif index == -1:
                if self.head == self.tail:
                    self.head.next=None
                    self.head.prev = None
                    self.head = None
                    self.tail = None
                else:
                    
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
                    
            else:
                tnode = self.head
                li=0
                
                while li<index-1:
                    if tnode.next == self.tail:
                        print("byeeeee")
                        return "byeeeee"
                    
                    tnode = tnode.next
                    li+=1
                nnode=tnode.next
                tnode.next=nnode.next
                nnode.next.prev=tnode
                
    def delAll(self):
        if self.head is None:
            return "CDLL not existing"
        else:
            self.tail.next = None
            tnode = self.head
            while tnode is not None:
                tnode.prev=None
                if tnode.next == self.tail:
                    print("byeeeee")
                    break  
                tnode = tnode.next
            self.head = None
            self.tail = None            
                
                
                    
                    

            
        
                
            
        

curcuDLL = CirDLL()
print(curcuDLL.CreateCDLL(9))
print(curcuDLL.insertCDLL(0,0))
print(curcuDLL.insertCDLL(2,0))
print(curcuDLL.insertCDLL(4,1))
print(curcuDLL.insertCDLL(7,1))
print([node.value for node in curcuDLL])
print(curcuDLL.travCDLL())
print(curcuDLL.revTravCDLL())
print(curcuDLL.searchCDLL(4)) 
print([node.value for node in curcuDLL])
print(curcuDLL.delCDLL(5))
print([node.value for node in curcuDLL])
print(curcuDLL.delAll())
print([node.value for node in curcuDLL])
print([node.value for node in curcuDLL])