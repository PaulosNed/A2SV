class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        n = len(pref)
        res = [0] * n
        x = 0
        for i in range(n):
            res[i] = x ^ pref[i]
            x ^= res[i]
        
        return res