class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        def dist(x1,x2,y1,y2):
            return abs(x1-x2)+abs(y1-y2)      
  
        self.ans = abs(start[0]-target[0]) + abs(start[1]-target[1])
        hm = dict()

        def helper(curX, curY, curDist):
            
            if curDist >= self.ans: 
                return
            
            self.ans = min(self.ans, dist(curX, target[0], curY, target[1]) + curDist)
            
            if (curX, curY) in hm:
                if hm[(curX,curY)] <= curDist:
                    return
            
            hm[(curX,curY)] = curDist
            
            for next in specialRoads:
                helper(next[2], next[3], curDist + dist(curX, next[0], curY, next[1]) + next[4])

        helper(start[0], start[1], 0)

        return self.ans