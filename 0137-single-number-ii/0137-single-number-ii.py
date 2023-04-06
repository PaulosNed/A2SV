class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) == 1:
            return nums[0]
        idx = 2
        while(idx < len(nums)):
            curr = nums[idx] ^ nums[idx-1] ^ nums[idx-2]
            if curr != nums[idx]:
                return curr
            idx += 3
        return nums[-1]