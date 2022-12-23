from math import log2
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        ans = 0
        dictD = Counter(deliciousness)
        powers = [i for i in range(22)]
        # checked = set()
        for item in deliciousness:
            dictD[item] -= 1
            for power in powers:
                temp = 2**power - item
                ans += dictD.get(temp, 0)
        return ans % (10**9 + 7)