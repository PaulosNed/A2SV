class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        def binarySearch(start, target):
            
            left = start
            right = len(nums) - 1
            
            while left <= right:
                
                mid = left + (right - left) // 2
                
                if target > nums[mid]:
                    left = mid + 1
                
                else:
                    right = mid - 1
                
            return right
        
        nums.sort()
        
        ans = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                target = nums[i] + nums[j]
                nxt = binarySearch(j + 1, target)
                ans += nxt - j
        
        return ans
                
                
                