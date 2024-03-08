class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count  = Counter(nums)
        max_value = max(count.values())
        
        ans = 0
        for key, value in count.items():
            if value == max_value:
                ans += value
        
        return ans