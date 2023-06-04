# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        sums = set()
        
        def traverse(root):
            if not root:
                return 0
            
            left = traverse(root.left)
            right = traverse(root.right)
            
            final = max(root.val, root.val + max(left, right))
            sums.add(final)
            sums.add(root.val + left + right)
            
            return final
            
            
            
        traverse(root)
        return max(sums) 