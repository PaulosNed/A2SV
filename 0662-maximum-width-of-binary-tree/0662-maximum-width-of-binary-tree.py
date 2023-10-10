# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        levels = defaultdict(lambda: [inf, -inf])
        
        def recurse(node, idx, level):
            
            if not node:
                return
            
            levels[level][0] = min(levels[level][0], idx)
            levels[level][1] = max(levels[level][1], idx)
            
            recurse(node.left, 2 * idx + 1, level + 1)
            recurse(node.right, 2 * idx + 2, level + 1)
            
            
            
        recurse(root, 0, 1)
        
        ans = 0
        
        for k in levels:
            ans = max(ans, levels[k][1] - levels[k][0] + 1)
        
        return ans
            