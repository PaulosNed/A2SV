class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:

        memo = {}

        for num in arr:
            if num - difference in memo:
                memo[num] = memo[num - difference] + 1
            else:
                memo[num] = 1
        
        return max(memo.values())