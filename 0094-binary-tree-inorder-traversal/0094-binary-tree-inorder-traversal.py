# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.calc(root, [])
    
    def calc(self, root, stack):
        if not root:
            return stack
        
        left = self.calc(root.left, stack)
        stack.append(root.val)
        right = self.calc(root.right, stack)
            
        return stack
        