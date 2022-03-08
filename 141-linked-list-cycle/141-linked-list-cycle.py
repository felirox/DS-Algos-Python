# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        loopL=head
        i=[]
        while loopL:
            if loopL in i:
                return True
            i.append(loopL)
            loopL=loopL.next
        return False
            
        