# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        
        def traverse(root, path):
            path.append(str(root.val))
            
            if not root.left and not root.right:
                paths.append(path[:])
                return
            
            if root.left:
                left = traverse(root.left, path[:])
            if root.right:
                right = traverse(root.right, path[:])
            
            return
            
            return
            
        traverse(root, [])
        ans = []
        for p in paths:
            ans.append("->".join(p))
        return ans
        
        