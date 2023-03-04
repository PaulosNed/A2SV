class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums) - 1
        while(start <= end):
            mid = start + (end - start) // 2
            if nums[start] == nums[end] == nums[mid] == target:
                return [start, end]
            elif nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                if nums[start] != target:
                    start += 1
                if nums[end] != target:
                    end -= 1
                    
        return [-1, -1]