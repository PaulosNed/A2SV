"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        def recurse(node):
            if not node:
                return []
            
            ans = [node.val]
            
            for child in node.children:
                ans.extend(recurse(child))
                
            return ans
        
        return recurse(root)