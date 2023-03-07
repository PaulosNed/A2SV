# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = self.calc(root)
        final = []
        if ans:
            for a in ans:
                final.append(a.val)
        return final
        
    def calc(self, root):
        if not root:
            return None
        
        left = self.calc(root.left)
        right = self.calc(root.right)
        ans = []
        if left:
            for l in left:
                ans.append(l)
        
        if root:    
            ans.append(root)
            
        if right:
            for r in right:
                ans.append(r)
            
        return ans
        