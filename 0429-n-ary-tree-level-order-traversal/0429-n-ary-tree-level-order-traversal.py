"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        levels = defaultdict(list)
        
        def recurse(node, level):
            if not node:
                return
            
            levels[level].append(node.val)
            
            for child in node.children:
                recurse(child, level + 1)
            
        recurse(root, 0)
        
        return list(levels.values())