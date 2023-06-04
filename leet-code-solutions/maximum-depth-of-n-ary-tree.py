"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        depth = 0
        
        def dfs(root, curr):
            nonlocal depth
            
            if not root:
                depth = max(curr, depth)
                return
            
            for child in root.children:
                dfs(child, curr + 1)
            
            depth = max(curr + 1, depth)
            
        dfs(root, 0)
        return depth