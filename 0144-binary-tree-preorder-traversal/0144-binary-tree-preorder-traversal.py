# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        queue = [root]
        final = []
        while queue:
            root = queue.pop()
            if root == None:
                continue
            queue.append(root.right)
            queue.append(root.left)
            final.append(root.val)
        return final