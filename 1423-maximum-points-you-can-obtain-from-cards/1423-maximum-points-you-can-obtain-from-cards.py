class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if len(cardPoints) == k:
            return sum(cardPoints)
        start = 0
        end = len(cardPoints) - k - 1
        minSum = float("inf")
        temp = sum(cardPoints[start:end+1])
        while end < len(cardPoints):
            minSum = min(minSum, temp)
            temp -= cardPoints[start]
            start += 1
            end += 1
            if end < len(cardPoints):
                temp += cardPoints[end] 
        return sum(cardPoints) - minSum