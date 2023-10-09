# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        
        ans = []
        def recurse(node, rem, curr):
            nonlocal root
            
            if not node:
                return
            
            if rem - node.val == 0 and not node.left and not node.right:
                curr.append(node.val)
                ans.append(curr[:])
                
            curr.append(node.val)
            recurse(node.left, rem - node.val, curr[:])
            recurse(node.right, rem - node.val, curr[:])
        
        recurse(root, targetSum, [])
        return ans
            
            
            
            
            
                