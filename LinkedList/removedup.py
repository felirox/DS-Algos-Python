from linkedlist import LinkedList

def removedup(ll):
    if ll.head is None:
        return "bruh"
    else:
        currentN=ll.head
        visited = set([currentN.value])
        while currentN.next:
            if currentN.next.value in visited:
                currentN.next = currentN.next.next
            else:
                visited.add(currentN.next.value)
                currentN=currentN.next
        return ll

def removedupno(ll):
    if ll.head is None:
        return "bruh"
    else:
        currentN=ll.head
        while currentN:
            runner=currentN
            while runner.next:
                if runner.next.value == currentN.value:
                    runner.next = runner.next.next
                else:
                    runner=runner.next
            currentN=currentN.next
        return ll.head
                    
                    
    
customLL = LinkedList()
customLL.generate(10,0,99)
print(customLL)
print(removedup(customLL))
print(customLL)