class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        stack = []
        final = [None] * len(nums)
        final2 = [None] * len(nums)
        
        for idx, val in enumerate(nums):
            while stack and stack[-1][1] < val:
                i, v = stack.pop()
                final[i] = idx
            
            stack.append([idx, val])
        
        stack = []
        for idx in range(len(nums)-1, -1, -1):
            while stack and nums[idx] < stack[-1][1]:
                i, v = stack.pop()
                final2[i] = idx
            
            stack.append([idx, nums[idx]])
        
        # print(final, final2)
        for i in range(len(final)):
            if final[i] != None and final2[i] != None:
                return True
        return False
                