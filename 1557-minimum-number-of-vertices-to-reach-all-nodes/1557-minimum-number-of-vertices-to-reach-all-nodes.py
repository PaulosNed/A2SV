class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        invalid = set()
        for edge in edges:
            invalid.add(edge[1])
        
        ans = []
        for i in range(n):
            if i not in invalid:
                ans.append(i)
        
        return ans