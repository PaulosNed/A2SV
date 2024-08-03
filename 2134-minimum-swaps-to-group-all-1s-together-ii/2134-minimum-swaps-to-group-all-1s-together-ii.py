class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        oneCnt = sum(nums)
        start = 0
        end = oneCnt 
        
        currCnt = sum(nums[:end])
        swaps = float("inf")
        
        nums += nums
        while end < len(nums):
            swaps = min(swaps, oneCnt - currCnt)
            
            if nums[end]:
                currCnt += 1
            
            if nums[start]:
                currCnt -= 1
            
            start += 1
            end += 1
        
        return swaps