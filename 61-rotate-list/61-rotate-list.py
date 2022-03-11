# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None or k==0:
            return head
        l=[]
        move=head
        while move:
            l.append(move.val)
            move=move.next
        km=k%len(l)
        for _ in range(km):
            p=l.pop()
            l.insert(0,p)
        head.val=None
        head.next=None
        head=None
        
        newll=ListNode(l.pop(0))
        travl=newll
        while l:
            travl.next=ListNode(l.pop(0))
            travl=travl.next
        return newll