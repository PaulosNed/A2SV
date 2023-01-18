class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        length = len(nums)
        for i in range(length):
            currStr = str(nums[i])
            currNum = int(currStr[::-1])
            nums.append(currNum)
        checker = set(nums)
        return len(checker)