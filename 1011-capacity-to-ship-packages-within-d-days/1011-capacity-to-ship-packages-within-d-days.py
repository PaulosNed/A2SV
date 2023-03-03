class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def countDays(weight):
            days = 0
            i = 0
            while i < len(weights):
                sum_ = 0
                while i < len(weights) and sum_ + weights[i] <= weight:
                    sum_ += weights[i]
                    i += 1
                days += 1
            return days
        
        start = max(weights)
        end = sum(weights)
        while(start <= end):
            mid = start + ((end - start)//2)
            if countDays(mid) <= days:
                end = mid - 1
            else:
                start = mid + 1
        return start
    
    