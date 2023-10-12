# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        cnt = 0
        
        def dfs(node):
            nonlocal cnt
            
            if not node:
                return 0
            
            opt1 = dfs(node.left)
            opt2 = dfs(node.right)
            
            cnt += abs(opt1)
            cnt += abs(opt2)
            
            return node.val - 1 + opt1 + opt2
    
        dfs(root)
        return cnt
            
            