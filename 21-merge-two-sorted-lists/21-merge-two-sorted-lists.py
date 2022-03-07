# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l=[]
        l1=list1
        l2=list2
        while l1:
            l.append(l1.val)
            l1=l1.next
        while l2:
            l.append(l2.val)
            l2=l2.next
        l.sort()
        print(l)
        oplist=ListNode()
        lfin=oplist
        for i in l:
            lfin.next=ListNode(i)
            lfin=lfin.next
            
        return oplist.next