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
        
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        count = 0
        
        def countEquals(root):
            if not root:
                return
            
            nonlocal count
            vals = self.calc(root, [])
            avg = sum(vals) // len(vals)
            if root.val == avg:
                count += 1
            
            countEquals(root.left)
            countEquals(root.right)
            
        countEquals(root)
        return count
        