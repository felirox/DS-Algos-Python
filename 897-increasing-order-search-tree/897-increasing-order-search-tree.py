# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.maxn=[]
        def maxfinder(root):
            if root:
                maxfinder(root.right)
                maxfinder(root.left)
                self.maxn.append(root.val)
        maxfinder(root)
        newroot=TreeNode()
        iterr=newroot
        self.maxn.sort()
        oi=self.maxn.pop()
        for i in self.maxn:
            iterr.val=i
            iterr.right=TreeNode()
            iterr=iterr.right
        iterr.val=oi
        return newroot