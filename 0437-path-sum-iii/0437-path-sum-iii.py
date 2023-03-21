# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = 0
        
        def recurse(root, currSum, prefixSum):
            nonlocal count
            
            if not root:
                return
            
            currSum += root.val
            if currSum - targetSum in prefixSum:
                count += prefixSum[currSum - targetSum]
            prefixSum[currSum] += 1
            
            left = recurse(root.left, currSum, prefixSum.copy())
            right = recurse(root.right, currSum, prefixSum.copy())
            
            return
        ps = defaultdict(int)
        ps[0] = 1
        recurse(root, 0, ps)
        return count
        