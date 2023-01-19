class Solution(object):
    def sortColors(self, nums):
        ans = [0] * 3
        final = []
        for num in nums:
            ans[num] += 1
        for idx,val in enumerate(ans):
            for _ in range(val):
                final.append(idx)
        for i in range(len(nums)):
            nums[i] = final[i]