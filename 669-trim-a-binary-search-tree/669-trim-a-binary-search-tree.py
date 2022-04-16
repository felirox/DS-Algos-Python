# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def iterr(root):
            if not root : return root
            if root.val>high:
                return iterr(root.left)
            elif root.val<low:
                return iterr(root.right)
            else:
                root.left=iterr(root.left)
                root.right=iterr(root.right)
                return root
        
        return iterr(root)
        
                