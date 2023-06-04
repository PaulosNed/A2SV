class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        
        heapify(stones)
        while (len(stones) > 1):
            curr1 = -(heappop(stones))
            curr2 = -(heappop(stones))
            
            nxt = curr1 - curr2
            if nxt:
                heappush(stones, -nxt)
        
        return 0 if not stones else -stones[0]