# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = defaultdict(list)
        
        def findLevel(root, level):
            nonlocal levels
            if not root:
                return
            
            level += 1
            levels[level].append(root.val)
            
            left = findLevel(root.left, level)
            right = findLevel(root.right, level)
        
        findLevel(root, -1)
        ans = []    
        for key in sorted(levels):
            ans.append(levels[key])
        return ans
            
            
            