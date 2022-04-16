# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.count=0
        def initt(root):
            if root:
                initt(root.right)
                root.val+=self.count
                self.count=root.val
                initt(root.left)
        initt(root)
        return root
                
        