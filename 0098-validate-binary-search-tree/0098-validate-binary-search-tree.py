# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], s = -2**31 - 1, e = 2 ** 31 + 1) -> bool:
        
        if not root.left and not root.right:
            return True
        
        if not root.right:
            if s < root.left.val < root.val:
                return self.isValidBST(root.left, s, root.val)
            else:
                return False
        
        if not root.left:
            if root.val < root.right.val < e:
                return self.isValidBST(root.right, root.val, e)
            else:
                return False
        
        if s < root.left.val < root.val < root.right.val < e:
            left = self.isValidBST(root.left, s, root.val)
            right = self.isValidBST(root.right, root.val, e)
            return left and right
        
        else:
            return False