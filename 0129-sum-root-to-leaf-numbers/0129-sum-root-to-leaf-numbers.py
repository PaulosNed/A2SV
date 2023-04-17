# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        nums = []
        
        def backtrack(root, curr):
            if not root.left and not root.right:
                curr.append(str(root.val))
                nums.append("".join(curr[:]))
                return
            
            curr.append(str(root.val))
            if root.left:
                backtrack(root.left, curr[:])
            if root.right:
                backtrack(root.right, curr[:])
            
        backtrack(root, [])
        
        ans = 0
        for num in nums:
            ans += int(num)
        
        return ans
            