class Solution(object):
    def numberOfSubarrays(self, nums, k):
        odds = 0
        count = 0
        tracker = {0:1}
        for num in nums:
            if (num%2 == 1):
                odds += 1
                
            if odds-k in tracker:
                count+=tracker[odds-k]
                
            if odds not in tracker:
                tracker[odds] = 1
            else:
                tracker[odds] += 1
                
        return count