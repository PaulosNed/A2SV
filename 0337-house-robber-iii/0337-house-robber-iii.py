# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        @cache
        def dp(node, canRob):
            if not node:
                return 0
            
            if not canRob:
                return dp(node.left, True) + dp(node.right, True)
            else:
                option1 = dp(node.left, True) + dp(node.right, True)
                option2 = dp(node.left, False) + dp(node.right, False) + node.val
                return max(option1, option2)
        
        return dp(root, True)