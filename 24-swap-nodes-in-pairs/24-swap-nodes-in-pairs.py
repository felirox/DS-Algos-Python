# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        dumno=ListNode(0)
        dumno.next=head
        cur=dumno
        while cur.next and cur.next.next:
            f=cur.next
            s=cur.next.next
            cur.next=s
            f.next=s.next
            s.next=f
            cur=cur.next.next
        return dumno.next
            
        