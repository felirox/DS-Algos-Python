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
    def inSLL(self, value, loc):
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

    def TSLL(self):
        if self.head is None:
            print("SLL not existing")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next
    
    def ssll(self, nval):
        if self.head is None:
            print("SLL not existing")
        else:
            node= self.head
            while node is not None:
                if(node.value == nval):
                    return node
                node = node.next
            return "Not Found"
        
    def DelN(self,loc):
        if self.head is None:
            print("Nothig bro")
                     
sill = SLL()
sill.inSLL(1,0)
sill.inSLL(12,1)
sill.inSLL(251,1)
#some error? check later

#print([node.value for node in sill])
sill.TSLL()
print(sill.ssll(1))