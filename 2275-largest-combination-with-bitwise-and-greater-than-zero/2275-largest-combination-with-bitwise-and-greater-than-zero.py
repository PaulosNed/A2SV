class Solution:
    def largestCombination(self, A):
        return max(sum(1 << i & a > 0 for a in A) for i in range(30))    