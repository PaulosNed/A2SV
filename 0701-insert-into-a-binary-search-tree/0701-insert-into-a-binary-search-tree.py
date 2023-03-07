# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        head = root
        if not head:
            return TreeNode(val)
        
        if val > head.val:
            head.right = self.insertIntoBST(head.right, val)
            
        else:
            head.left = self.insertIntoBST(head.left, val)
            
        return root