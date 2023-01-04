class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        checker = set()
        for i in range(3):
            if (points[i][0], points[i][1]) in checker:
                return False
            checker.add((points[i][0], points[i][1]))
        if points[1][0]-points[0][0] == 0:
            m1 = None
        else:
            m1 = (points[1][1]-points[0][1]) / (points[1][0]-points[0][0])
        if points[2][0]-points[1][0] == 0:
            m2 = None
        else:
            m2 = (points[2][1]-points[1][1]) / (points[2][0]-points[1][0])
        if m1 == m2:
            return False
        return True