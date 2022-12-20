class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        dis = float("inf")
        idx = -1
        for i in range(len(points)):
            if points[i][0] == x or points[i][1] == y:
                currDis = abs(x - points[i][0]) + abs(y - points[i][1])
                if currDis < dis:
                    idx = i
                    dis = currDis
        return idx