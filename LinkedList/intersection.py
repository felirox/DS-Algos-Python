from linkedlist import LinkedList, Node


def intersection(llA, llB):
    if llA.tail is not llB.tail:
        return False
    lenA = len(llA)
    lenB= len(llB)
    
    shorter = llA if lenA<lenB else llB
    longer = llB if lenA<lenB else llA
    
    diff = len(longer)-len(shorter)
    longerNode = longer.head
    shorterNode = shorter.head
    
    for i in range(diff):
        longerNode = longerNode.next
    
    while shorterNode is not longerNode:
        shorterNode = shorterNode.next
        longerNode = longerNode.next
     
    return shorterNode



# Helpter Addn method

def sameNode(llA, llB, val):
    tempNode = Node(val)
    llA.tail.next = tempNode
    llA.tail = tempNode
    
    llB.tail.next = tempNode
    llB.tail = tempNode
    
llA = LinkedList()
llA.generate(4, 0, 19)

llB = LinkedList()
llB.generate(3, 0, 19) 

sameNode(llA, llB, 10)

print(llA)
print(llB)
   
print(intersection(llA, llB)    )