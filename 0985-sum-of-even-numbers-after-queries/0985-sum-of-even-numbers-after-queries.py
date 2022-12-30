class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        currSum = 0
        ans = []
        for num in nums:
            if num%2 == 0:
                currSum += num
        for query in queries:
            updatedValue = nums[query[1]] + query[0]
            if  nums[query[1]]%2 == 0:
                currSum -= nums[query[1]]
            if updatedValue%2 == 0:
                currSum += updatedValue
            nums[query[1]] = updatedValue
            ans.append(currSum)
        return ans