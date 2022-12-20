from math import comb
class Solution:
    def similarPairs(self, words: List[str]) -> int:
        wordsCount = {}
        ans = 0
        for s in words:
            temp1 = list(s)
            temp1.sort()
            temp1 = set(temp1)
            temp1 = tuple(temp1)
            wordsCount[temp1] = wordsCount.get(temp1, 0) + 1
        for key in wordsCount:
            if wordsCount[key] > 1:
                ans += comb(wordsCount[key], 2)
        
        return ans