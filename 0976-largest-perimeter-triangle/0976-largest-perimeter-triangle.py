class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        nums.sort()
        if len(nums) == 3:
            return sum(nums) if nums[0] + nums[1] > nums[2] else 0
        end = len(nums) - 1
        start = end-2
        perimeter = 0
        while(start >= 0):
            if nums[start] + nums[start+1] > nums[end]:
                return sum(nums[start:end+1])
            else:
                start -= 1
                end -= 1
        return perimeter