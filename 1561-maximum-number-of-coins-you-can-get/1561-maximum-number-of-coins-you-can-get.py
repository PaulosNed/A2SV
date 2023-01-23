class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        maxCoins = 0
        limit = len(piles)//3
        for i in range(limit):
            maxCoins+=piles[-2]
            piles.pop(0)
            piles.pop(-1)
            piles.pop(-1)
        return maxCoins