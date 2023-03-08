# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def calc(self, root, stack):
        if not root:
            return stack
        
        left = self.calc(root.left, stack)
        stack.append(root.val)
        right = self.calc(root.right, stack)
            
        return stack
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        vals = self.calc(root, [])
        return vals[k-1]