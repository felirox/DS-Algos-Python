from linkedlist import LinkedList

def sumofLL(lla,llb):
    n1=lla.head
    n2=llb.head
    carry=0
    ll=LinkedList()
    while n1 or n2:
        result=carry
        if n1:
            result+=n1.value
            n1=n1.next
        if n2:
            result+=n2.value
            n2=n2.next
        ll.add((int(result % 10)))
        carry = result/10
    return ll

lla=LinkedList()
lla.generate(5, 0, 9)
print(lla)
llb=LinkedList()
llb.generate(5, 0, 9)
print(llb)
print("lalala")
print(sumofLL(lla,llb))


            
            
        
        