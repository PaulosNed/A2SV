# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n=len(inorder)
        poststart=instart=0
        postend=inend=n-1
        d={}
        for i in range(n):
            d[inorder[i]]=i
        return self.constructTree(postorder,poststart,postend,inorder,instart,inend,d)
    
    def constructTree(self,postorder,poststart,postend,inorder,instart,inend,d):
        if poststart>postend or instart>inend:
            return None
        root=TreeNode(postorder[postend])
        elem=d[root.val]
        nelem=elem-instart
        root.left=self.constructTree(postorder,poststart,poststart+nelem-1,inorder,instart,elem-1,d)
        root.right=self.constructTree(postorder,poststart+nelem,postend-1,inorder,elem+1,inend,d)
        return root