class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        sortedHeap = []
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if len(sortedHeap) < k:
                    heappush(sortedHeap, -matrix[i][j])
                else:
                    heappushpop(sortedHeap, -matrix[i][j])
        
        return -sortedHeap[0]
        
        