# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        sum_ = 0
        
        def recurse(node, isLeft):
            nonlocal sum_
            
            if not node:
                return True
            
            left = recurse(node.left, True)
            right = recurse(node.right, False)
            
            if left and right and isLeft:
                sum_ += node.val
            
            return False
        
        recurse(root, False)
        return sum_