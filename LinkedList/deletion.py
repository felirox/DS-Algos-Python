class Node:
    def __init__(self, value=None):
        self.value=value
        self.next=None

class SLL:
    def __init__(self):
        self.head=None
        self.tail=None
    def __iter__ (self):
        node=self.head
        while node:
            yield node
            node = node.next
    def inSLL(self, value, loc): #insertion 
        newN = Node(value)
        if self.head is None:
            self.head=newN
            self.tail=newN
        else:
            if loc == 0:
                newN.next=self.head
                self.head=newN
            elif loc == -1:
                newN.next=None
                self.tail.next=newN
                self.tail = newN
            else:
                tNode = self.head
                index = 0
                while index < loc-1:
                    tNode = tNode.next
                    index+=1
                nNode = tNode.next
                tNode.next=newN
                newN.next = nNode
                if tNode == self.tail:
                    self.tail=newN

    def TSLL(self): #traversal
        if self.head is None:
            print("SLL not existing")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next
    
    def ssll(self, nval): #search
        if self.head is None:
            print("SLL not existing")
        else:
            node= self.head
            while node is not None:
                if(node.value == nval):
                    return node
                node = node.next
            return "Not Found"
        
    def DelN(self,loc): #delete a node with a given location
        if self.head is None:
            print("Nothig bro")
        else:
            if loc == 0:
                if self.head == self.tail:    
                    self.head=None
                    self.tail=None
                else:
                    self.head = self.head.next
            elif loc == -1:
                if self.head == self.tail:    
                    self.head=None
                    self.tail=None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node=node.next
                    node.next=None
                    self.tail = node
            else:
                tempNode = self.head
                index=0
                while index <loc-1:
                    tempNode = tempNode.next
                    index+=1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
                
           
    def DelFullSLL(self): #deleting entire SLL
        if self.head is None:
            print("SLL does not exist")
        else:
            self.head=None
            self.tail=None
            print("SLL deleted")
        
    
                
sill = SLL()
sill.inSLL(1,0)
sill.inSLL(12,1)
sill.inSLL(251,1)
sill.inSLL(12,1)
sill.inSLL(251,1)
#some error? check later

print([node.value for node in sill])
#sill.TSLL()
#sill.DelN(0)
#sill.TSLL()
print(sill.ssll(12))
print([node.value for node in sill])
sill.DelFullSLL()

#sill.DelFullSLL()
#sill.DelFullSLL()
#sill.DelN(-1)
