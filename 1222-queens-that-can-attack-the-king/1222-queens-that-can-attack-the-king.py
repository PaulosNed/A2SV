class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        x = king[0]
        y = king[1]
        direction = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]
        ans = []
        allQueens = set()
        for queen in queens:
            allQueens.add(tuple(queen))
        for i in range(8):
            currCheck = direction[i]
            while(0 <= x-currCheck[0] <= 8) and (0 <= y-currCheck[1] <= 8):
                curr = (x-currCheck[0], y-currCheck[1])
                if curr in allQueens:
                    ans.append(list(curr))
                    break
                currCheck = [currCheck[0]+direction[i][0], currCheck[1]+direction[i][1]]
        return ans