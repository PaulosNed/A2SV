from typing import List
from collections import *
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    
	    indegree = [0 for _ in range(V)]
	    
	    for i, neighbours in enumerate(adj):
	        for neighbour in neighbours:
	            indegree[i] += 1
	            indegree[neighbour] += 1
	    for i in range(len(indegree)):
	        indegree[i] = indegree[i] // 2
	        
	    queue = deque([])
        visited = set()
	    
        for node in range(len(adj)):
            if indegree[node] < 2:
                queue.append(node)
                visited.add(node)
        
        while queue:
            curr = queue.popleft()
            
            for neighbour in adj[curr]:
                indegree[neighbour] -= 1
                
                if indegree[neighbour] < 2 and neighbour not in visited:
                    queue.append(neighbour)
                    visited.add(neighbour)
            
        # print(adj, indegree, visited)
        return len(visited) != V
    
    
    


#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends