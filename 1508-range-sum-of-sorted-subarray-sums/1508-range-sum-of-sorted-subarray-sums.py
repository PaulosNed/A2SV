class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        
        sumArr = []
        
        for i in range(len(nums)):
            
            currSum = 0 
            
            for j in range(i, len(nums)):
                currSum += nums[j]
                sumArr.append(currSum)
        
        sumArr.sort()
        return sum(sumArr[left - 1 : right]) % (10**9 + 7)