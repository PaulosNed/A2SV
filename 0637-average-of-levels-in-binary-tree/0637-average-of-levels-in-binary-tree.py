# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([[root]])
        avg = []
        while queue:
            curr = queue.popleft()
            
            total = 0
            count = len(curr)
            nxt = []
            for node in curr:
                total += node.val
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            
            avg.append(total / count)
            if nxt:
                queue.append(nxt)
        
        return avg
            