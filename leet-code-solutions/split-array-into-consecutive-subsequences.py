class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        
        sub = defaultdict(int)
        rem = Counter(nums)
        
        for num in nums:
            if not rem[num]:
                continue
            
            if sub[num-1]:
                sub[num-1] -= 1
                sub[num] += 1
                rem[num] -= 1
            
            elif not rem[num+1] or not rem[num+2]:
                return False
            
            else:
                rem[num + 1] -= 1
                rem[num + 2] -= 1
                rem[num] -= 1
                sub[num + 2] += 1
        
        return True