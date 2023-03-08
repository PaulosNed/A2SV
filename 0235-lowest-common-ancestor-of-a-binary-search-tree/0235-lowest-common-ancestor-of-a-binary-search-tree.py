# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        final = None
        
        def findAncestor(root):
            nonlocal final
            found = 0
            if not root:
                return found
        
            if root.val == p.val or root.val == q.val:
                found += 1
                
            left = findAncestor(root.left)
            right = findAncestor(root.right)
            
            if left == right == 1:
                found = 1
                
            found += max(left, right)
            
            if found == 2 and not final:
                final = root
            
            return found
        
        findAncestor(root)
        return final
        