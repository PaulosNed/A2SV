class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        offset = 1950
        prefix_sum = [0] * (101)
        
        for y1, y2 in logs:
            prefix_sum[y1-offset] += 1
            prefix_sum[y2-offset] -= 1
        
        max_year = 0
        max_val = 0
        
        ps = 0
        for i, num in enumerate(prefix_sum):
            ps += num
            
            if ps > max_val:
                max_val = ps
                max_year = i
        
        return offset + max_year