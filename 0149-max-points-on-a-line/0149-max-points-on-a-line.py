class Solution:
    def maxPoints(self, points):
        same = 1
        for idx,value in enumerate(points[:-1]):
            slopes = {}
            duplicates = 1
            for x,y in points[idx+1:]:
                if value[0] == x and value[1] == y:
                    duplicates += 1
                m = (value[1] - y) / (value[0] -x) if value[0] != x else float("inf")
                slopes[m] = slopes.get(m, 0) + 1
            currSame = max(slopes.values()) + duplicates
            same = max(same, currSame)
        return same
        
                