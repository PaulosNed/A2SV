# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        return self.compare(root.left, root.right)
    
    def compare(self, root1, root2):
        if not root2 or not root1:
            return root1 == root2
        
        if root1.val != root2.val:
            return False
        
        a = self.compare(root1.left, root2.right)
        b = self.compare(root1.right, root2.left)
        
        return a and b