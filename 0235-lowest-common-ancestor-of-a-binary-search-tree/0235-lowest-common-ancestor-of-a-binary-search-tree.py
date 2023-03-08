# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        test1 = p.val < root.val and q.val < root.val
        test2 = p.val > root.val and q.val > root.val
        
        if not(test1 or test2):
            return root
        
        if root.val == p.val or root.val == q.val:
            return root
        
        if test1:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)