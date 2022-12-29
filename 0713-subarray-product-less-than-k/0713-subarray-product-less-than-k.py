class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        i, j = 0, 0
        product = 1
        subarrays = 0
        while j < len(nums):
            if j < len(nums) - 1 and product * nums[j] < k:
                product *= nums[j]
                j += 1
            elif i < j:
                subarrays += j - i
                if j == len(nums) - 1 and product * nums[j] < k:
                    subarrays += 1
                product //= nums[i]
                i += 1
            else:
                i += 1
                j += 1
        if nums[-1] < k:
            subarrays += 1
        return subarrays
