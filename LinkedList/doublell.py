#DoublyLinkedList
#Each node - 2 ref
# Can go forward/backward
class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
        self.prev=None
        
class DoubLL:
    def __init__(self):
        self.head=None
        self.tail=None
    def __iter__(self):
        currentnode=self.head
        while currentnode:
            yield currentnode
            currentnode=currentnode.next
    
    #Creation of Doubly Linked List
    def createDLL(self,nvalue):
        node=Node(nvalue)
        node.prev=None
        node.next=None
        self.head=node
        self.tail=node
        return "DLL created successfully"
    
    def insDLL(self,val,loc):
        if self.head is None:
            return "DLL is empty"
        else:
            nnode=Node(val)
            if loc==0:
                nnode.next=self.head
                nnode.prev=None
                self.head.prev=nnode
                self.head=nnode
            elif loc==-1:
                nnode.next=None
                nnode.prev=self.tail
                self.tail.next=nnode
                self.tail=nnode 
                
                
            else:
                inn=0
                tnode=self.head
                while(inn<loc-1):
                    tnode= tnode.next
                    inn+=1
                
                tnnode=tnode.next
                nnode.prev=tnode
                nnode.next=tnnode
                tnnode.prev=nnode
                tnode.next=nnode
    
    def travDLL(self):
        for node in self:
            if node.value is None:
                break
            else:
                print(node.value)
                
    def travxDLL(self):
        if self.head is None:
            return "DLL is empty"
        else:
            tnod=self.head
            while tnod:
                print(tnod.value)
                tnod=tnod.next
                
    def rtravDLL(self):
        if self.head is None:
            print("DLL empty")
        else:
            tnod=self.tail
            while tnod:
                if tnod.value == "None":
                    break
                print(tnod.value)
                tnod=tnod.prev
                
    def searchDLL(self,val):
        locx=0
        for node in self:
            
            if node.value==val:
                print(f"Value found at position {locx}" ) #For loop not working
                break
            locx+=1
    def delDLL(self,loc):
        if loc==0:
            if self.head == self.tail:
                self.head=None
                self.tail=None
            else:
                self.head.next.prev=None
                self.head=self.head.next
        elif loc==-1:
            if self.head == self.tail:
                self.head=None
                self.tail=None
            else:
                self.tail.prev.next=None
                self.tail=self.tail.prev
        else:
            ite=0
            ttemp=self.head
            while(ite<loc-1):
                ttemp=ttemp.next
                ite+=1
            ttemp.next=ttemp.next.next
            ttemp.next.prev=ttemp
    def delallDLL(self):
        for node in self:
            node.prev=None
        self.head=None
        self.prev=None
            
            
            
                

odll = DoubLL()
odll.createDLL(1)
print([node.value for node in odll])
odll.insDLL(2,0)
print([node.value for node in odll])
odll.insDLL(4,0)
print([node.value for node in odll])

odll.insDLL(3,1)
print([node.value for node in odll])
odll.delDLL(-1)
print("sum del")
print([node.value for node in odll])
print (odll.travxDLL()) #None gets printed for some reason hmmmm
print (odll.searchDLL(1)) 
odll.delallDLL()
print("baka")
print([node.value for node in odll])