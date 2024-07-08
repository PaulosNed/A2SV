class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        hashmap = collections.Counter(nums)
        numbers = 0
        if k == 0:
            for i in hashmap.values(): 
                if i > 1:
                    numbers += 1
            return numbers
        for i in hashmap:
            if i + k in hashmap:
                numbers += 1
        return numbers