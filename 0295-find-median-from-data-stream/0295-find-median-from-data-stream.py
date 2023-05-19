class MedianFinder:

    def __init__(self):
        self.nums = []
        self.size = 0
        self.heap = []

    def addNum(self, num: int) -> None:
        self.size += 1
        heappush(self.nums, num)
        if len(self.heap) < (self.size // 2) + 1:
            heappush(self.heap, -self.nums[0])
            heappop(self.nums)
            
        elif -self.heap[0] > num:
            popped = -heappop(self.heap)
            heappush(self.nums, popped)
            heappush(self.heap, -self.nums[0])
            heappop(self.nums)
            
    def findMedian(self) -> float:
        if self.size % 2 != 0:
            return -self.heap[0]
        
        else:
            mid1 = -heappop(self.heap)
            ans = (mid1 - self.heap[0]) / 2
            heappush(self.heap, -mid1)
            return ans
        
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()