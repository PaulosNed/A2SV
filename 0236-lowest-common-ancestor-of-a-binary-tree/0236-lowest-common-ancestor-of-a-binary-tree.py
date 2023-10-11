# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None
        
        def recurse(node):
            nonlocal ans
            
            if not node:
                return False, False
            
            foundP, foundQ = False, False
            
            if p.val == node.val:
                foundP = True
            
            if q.val == node.val:
                foundQ = True
            
            opt1P, opt1Q = recurse(node.left)
            opt2P, opt2Q = recurse(node.right)
            
            ansP = foundP or opt1P or opt2P
            ansQ =foundQ or opt1Q or opt2Q
            
            if not ans and ansP and ansQ:
                ans = node
            
            return ansP, ansQ
        
        recurse(root)
        return ans
                