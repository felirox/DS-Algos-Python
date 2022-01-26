class Node:
    def __init__(self,value=None):
        self.value = value
        self.next=None
        
class CirSLL:
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
            
            
    #Creation of Circular Single Linked List
    def createSLL(self,nodeVal):
        node=Node(nodeVal)
        node.next=node
        self.head=node
        self.tail=node
        return "CSLL created"
    
    def insertSLL(self,nodeVal, loc: int):
        if self.head is None:
            return "SLL does not exist"
        else:
            nnode=Node(nodeVal)
            if loc == 0:
                nnode.next=self.head
                self.head=nnode
                self.tail.next=nnode
            elif loc == -1:
                nnode.next=self.tail.next
                self.tail.next=nnode
                self.tail=nnode
            else:
                tnode = self.head
                index=0
                while index<loc-1:
                    tnode=tnode.next
                    index+=1
                nxnode=tnode.next#nx-next node
                tnode.next=nnode
                nnode.next=nxnode
            return "Node has been successfully inserted"
    def traverseSLL(self): #using for loop
        if self.head is None:
            return "SLL does not exist"       
        else:
            for node in self:   #THIS IS AMMMAAZEEEEE
                print(node.value)
                #if node.next == self.head:
                    #break        
            return "Traversal completefg"
        
    def othertraverseSLL(self): #using while loop - Meh
        if self.head is None:
            return "SLL does not exist"       
        else:
            tnode=self.head
            while tnode:
                print(tnode.value)
                tnode=tnode.next
                if tnode == self.tail.next:
                    break
                
                       
            return "Traversal complete"        
        
    def searchSll(self,nodeVal):
        
        if self.head is None:
            return "SLL does not exist"
        else:
            index=0
            for node in self:
                if node.value==nodeVal:
                    return f"Found value at {index}"
                index+=1
            return "Value not found"
        
    def deleteSll(self,index): #deletes part of the SLL
        if self.head is None:
            return "SLL does not exist"       
        else:
            if index == 0:
                if self.head == self.tail:
                    self.head.next=None
                    self.head = None
                    self.tail=None
                else:
                    self.head = self.head.next
                    self.tail.next=self.head
            elif index==-1:
                if self.head == self.tail:
                    self.head.next=None
                    self.head = None
                    self.tail=None
                else:
                    node = self.head
                    while node is not None :
                        if node.next==self.tail: #tail coz we want to compare node to see if it is last
                            break
                        node=node.next
                    node.next=self.head     #or it can be self.head               
                    self.tail=node       
            else:
                tnode=self.head
                linde =0
                while linde<index-1:       
                    tnode=tnode.next
                    linde+=1
                nnode=tnode.next
                tnode.next=nnode.next
            return f"{index} Deleted"
    
    def delWhSLL(self): #Delete entire SLL
        if self.head is None:
            return "SLL does not exist"
        else:
            self.head=None
            self.tail.next=None
            self.tail=None
            return "Whole CSLL has been successfully deleted"
                    
                
                
                    
                            
                                    
                    
        

ocsll  = CirSLL()
print(ocsll.createSLL(1))
print([node.value for node in ocsll ]) #1
print(ocsll.insertSLL(2,-1))
print([node.value for node in ocsll ]) #1
print(ocsll.insertSLL(5,1))
print([node.value for node in ocsll ]) #1
print(ocsll.deleteSll(1))
print([node.value for node in ocsll ]) #1
print(ocsll.insertSLL(7,2))
print([node.value for node in ocsll ]) #1
print(ocsll.insertSLL(3,-1))
print([node.value for node in ocsll ]) #1

print(ocsll.traverseSLL())
print([node.value for node in ocsll ]) #1
print(ocsll.deleteSll(2))
print([node.value for node in ocsll ]) #1
print(ocsll.searchSll(5))
print([node.value for node in ocsll ]) #1
print(ocsll.delWhSLL())
print([node.value for node in ocsll ]) #1