# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pQueue = [p]
        qQueue = [q]
        while(pQueue and qQueue):
            p = pQueue.pop(0)
            q = qQueue.pop(0)
            if p == q == None:
                continue
            elif p == None or q == None:
                return False
            if p.val != q.val:
                return False
            pQueue.append(p.left)
            pQueue.append(p.right)
            qQueue.append(q.left)
            qQueue.append(q.right)
        if p != q:
            return False
        if len(pQueue) != len(qQueue):
            return False
        return True