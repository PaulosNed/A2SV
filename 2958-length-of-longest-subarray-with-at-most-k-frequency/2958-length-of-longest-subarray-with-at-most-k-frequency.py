class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        start = 0
        end = 0
        
        tracker = defaultdict(int)
        
        i = 0
        max_len = 0
        
        while end < len(nums):
            # print(start, end, tracker)
            
            if tracker[nums[end]] + 1 > k:
                max_len = max(max_len, end - start)
                tracker[nums[start]] -= 1
                start += 1
            
            else:
                tracker[nums[end]] += 1
                end += 1
        
        max_len = max(max_len, end - start)
        return max_len