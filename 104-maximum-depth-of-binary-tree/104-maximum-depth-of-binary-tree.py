# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
maxd=0
class Solution:
    def sloop(self,level,md):
        if level is None:
            return 
        global maxd
        maxd=max(maxd,md)
        self.sloop(level.left,md+1)
        self.sloop(level.right,md+1)
        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        global maxd
        maxd=0        
        self.sloop(root,1)
        return maxd
        