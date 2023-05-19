class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        tracker = []
        
        for i in range(1, len(heights)):
            dif = heights[i] - heights[i-1]
            if dif > 0:
                if dif <= bricks:
                    heappush(tracker, -dif)
                    bricks -= dif
                else:
                    if not ladders:
                        return i - 1
                    ladders -= 1
                    if tracker:
                        if dif < -tracker[0]:
                            max_bricks = -heappop(tracker)
                            heappush(tracker, -dif)
                            bricks += max_bricks - dif
                    
        return len(heights) - 1