class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x:x[1])
        arrows = 0
        start = 0
        end = 1
        while (end < len(points)):
            if points[start][1] < points[end][0]:
                arrows += 1
                start = end
            end += 1
        return arrows + 1