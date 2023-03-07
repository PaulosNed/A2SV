# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.recursiveCount(root, 0)
    
    def recursiveCount(self, root, count):
        if not root:
            return count
        
        left = self.recursiveCount(root.left, count + 1)
        right = self.recursiveCount(root.right, count + 1)
        
        return max(left, right)