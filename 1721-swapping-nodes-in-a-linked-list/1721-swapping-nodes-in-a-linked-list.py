# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ite=head
        count=0
        kth=0
        while ite:
            count+=1
            if count ==k:
                kth=ite
            ite=ite.next
        ite=head
        iter=0
        while ite:
            iter+=1
            if count-k+1 ==iter:
                kth.val,ite.val=ite.val,kth.val
            ite=ite.next
        return head
        