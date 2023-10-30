class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            if target - num == num:
                nums.pop(i)
                if num in set(nums):
                    j = nums.index(target - num)
                    return [i, j+1]
                else:
                    nums.insert(i, num)
                    continue
            if target - num in set(nums[:i]+nums[i+1:]):
                j = nums.index(target - num)
                return [i,j]