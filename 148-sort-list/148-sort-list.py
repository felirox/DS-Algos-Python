# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=[]
        iterr=head
        
        while iterr:
            l.append(iterr.val)
            iterr=iterr.next
        l.sort()
        iterr=head
        i=0
        while iterr:
            iterr.val=l[i]
            iterr=iterr.next
            i+=1
        return head