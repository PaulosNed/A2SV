# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        def traverse(root):
            if not root:
                return
            
            if root.left:
                graph[root.val].append(root.left.val)
                graph[root.left.val].append(root.val)
            
            if root.right:
                graph[root.val].append(root.right.val)
                graph[root.right.val].append(root.val)
            
            traverse(root.left)
            traverse(root.right)
        
        graph = defaultdict(list)
        traverse(root)
        queue = deque([target.val])
        visited = {target.val}
        
        for _ in range(k):
            size = len(queue)
            
            for _ in range(size):
                curr = queue.popleft()
                
                for neighbour in graph[curr]:
                    if neighbour not in visited:
                        queue.append(neighbour)
                        visited.add(neighbour)
        
        return list(queue)
            
            