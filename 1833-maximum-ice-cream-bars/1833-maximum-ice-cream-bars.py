class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        bars = 0
        currSum = 0
        for cost in costs:
            if cost+currSum > coins:
                return bars
            bars += 1
            currSum += cost
        return bars