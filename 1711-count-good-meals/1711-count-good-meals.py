from math import log2
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        ans = 0
        dictD = Counter(deliciousness)
        powers = [2**i for i in range(22)]
        for item in deliciousness:
            dictD[item] -= 1
            for power in powers:
                adjacent = power - item
                ans += dictD.get(adjacent, 0)
        return ans % (10**9 + 7)