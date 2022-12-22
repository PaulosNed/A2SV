from math import log2
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        ans = 0
        dictD = Counter(deliciousness)
        setD = set(deliciousness)
        powers = [i for i in range(22)]
        checked = set()
        for item in setD:
            for power in powers:
                temp = 2**power - item
                if temp == item:
                    ans += comb(dictD[item], 2)
                elif temp in setD:
                    checker = (temp, item) if temp < item else (item, temp)
                    if checker in checked:
                        continue
                    ans += (dictD[item] * dictD[temp])
                    checked.add(checker)
        return ans % (10**9 + 7)