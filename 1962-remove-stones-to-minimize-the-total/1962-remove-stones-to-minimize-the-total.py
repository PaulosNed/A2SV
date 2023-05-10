class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        for i in range(len(piles)):
            piles[i] = -piles[i]
            
        heapify(piles)
        
        for _ in range(k):
            curr = -heappop(piles)
            curr -= floor(curr / 2)
            heappush(piles, -curr)
        
        return -sum(piles)