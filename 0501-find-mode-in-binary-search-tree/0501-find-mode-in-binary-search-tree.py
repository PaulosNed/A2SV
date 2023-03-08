# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        tracker = defaultdict(int)
        
        def mode(root):
            nonlocal tracker
            if not root:
                return
            
            tracker[root.val] += 1
            mode(root.left)
            mode(root.right)
        
        mode(root)
        modeValue = max(tracker.values())
        final = []
        for key in tracker:
            if tracker[key] == modeValue:
                final.append(key)
        return final
            