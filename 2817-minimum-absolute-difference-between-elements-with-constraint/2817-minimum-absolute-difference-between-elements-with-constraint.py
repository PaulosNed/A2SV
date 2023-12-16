from sortedcontainers import SortedList

class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        
        options = SortedList()
        
        ptr = len(nums) - x - 1
        options.add(nums[-1])
        ans = float("inf")
        curr_idx = len(nums) - 2
        
        while ptr >= 0:
            idx = bisect_left(options, nums[ptr])
            idx = max(1, idx)
            idx = min(idx, len(options) - 1)
            ans = min(ans, abs(nums[ptr] - options[idx]), abs(nums[ptr] - options[idx - 1]))
            options.add(nums[curr_idx])
            curr_idx -= 1
            ptr -= 1
        
        return ans
            