# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        ans = 0
        
        def dfs(root, flag):
            nonlocal ans
            
            if not root:
                return
            
            if flag:
                if root.left:
                    ans += root.left.val
                if root.right:
                    ans += root.right.val
                
            if root.val%2 == 0:
                flag = True
            else:
                flag = False
            
            dfs(root.left, flag)
            dfs(root.right, flag)
        
        dfs(root, False)
        return ans