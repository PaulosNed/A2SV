class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def findSum(mid):
            sum_ = 0
            for num in nums:
                sum_ += ceil(num / mid)
            return sum_
        
        start = 1
        end = max(nums)
        while(start <= end):
            mid = start + (end - start) // 2
            if findSum(mid) > threshold:
                start = mid + 1
            else:
                end = mid - 1
                
        return start
        