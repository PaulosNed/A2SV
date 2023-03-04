class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def countBananas(mid):
            i = 0
            count = 0
            while(i < len(piles)):
                count += (ceil(piles[i] / mid))
                i += 1
            
            return count
                    
            
        left = 1
        right = sum(piles)
        while(left <= right):
            mid = left + ((right - left) // 2)
            if countBananas(mid) > h:
                left = mid + 1
            else:
                right = mid - 1
        return left