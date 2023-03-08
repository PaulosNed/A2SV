# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def calc(self, root, stack, k):
        if not root:
            return stack
        if len(stack) == k:
            return stack
        
        left = self.calc(root.left, stack, k)
        stack.append(root.val)
        right = self.calc(root.right, stack, k)
            
        return stack
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        vals = self.calc(root, [], k)
        return vals[k-1]