class Solution(object):
    def maxOperations(self, nums, k):
        count = 0
        nums.sort()
        start = 0
        end = len(nums) - 1
        while(start < end):
            if nums[start]+nums[end] < k:
                start += 1
            elif nums[start]+nums[end] > k:
                end -= 1
            else:
                count += 1
                start += 1
                end -= 1
        return count