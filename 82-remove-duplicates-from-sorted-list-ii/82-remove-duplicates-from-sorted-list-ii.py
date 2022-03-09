# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel=ListNode(0,head)
        prev=sentinel
        bhead=head
        while bhead:
            if bhead.next and bhead.val==bhead.next.val:
                while bhead.next and bhead.val==bhead.next.val:
                    bhead=bhead.next
                prev.next=bhead.next
            else:
                prev=prev.next
                
            bhead=bhead.next
            
            
        return sentinel.next