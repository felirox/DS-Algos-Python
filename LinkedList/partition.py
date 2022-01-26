from linkedlist import LinkedList

def partition (ll,x):
    curNode = ll.head
    ll.tail = ll.head
    
    while curNode:
        nextNode = curNode.next
        curNode.next = None
        if curNode.value <x:
            curNode.next=ll.head
            ll.head = curNode
        else:
            ll.tail.next=curNode
            ll.tail=curNode
        curNode = nextNode
        
    if ll.tail.next is not None:
        ll.tail.next = None
    
cusLL = LinkedList()
cusLL.generate(10,0,100)
print(cusLL)
partition(cusLL,50)
print(cusLL)            
            