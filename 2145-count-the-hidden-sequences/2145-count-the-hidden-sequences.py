class Solution:
    def numberOfArrays(self, diff, lower, upper):
        A = list(accumulate(diff, initial = 0))
        return max(0, (upper - lower) - (max(A) - min(A)) + 1)
