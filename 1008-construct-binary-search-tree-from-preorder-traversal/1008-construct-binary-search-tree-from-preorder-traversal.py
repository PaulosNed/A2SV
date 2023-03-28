# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, A):
        if len(A) == 1:
            return TreeNode(A[0])
        
        stack = []
        ans = None
        last = None
        for i, v in enumerate(A):
            curr = TreeNode(v)
            while stack and v > stack[-1].val:
                popped = stack.pop()
                last = popped
                if popped.val == A[0]:
                    ans = popped
                if stack and not stack[-1].left:
                    stack[-1].left = popped
                if not stack or stack[-1].val > v:
                    popped.right = curr
                    
            stack.append(curr)
        
        
        if len(stack) > 1:
            while len(stack) > 1:
                popped = stack.pop()
                if stack and not stack[-1].left:
                    stack[-1].left = popped
        
        if not ans:
            return stack[-1]
        return ans