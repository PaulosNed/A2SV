class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ctr=0
        sumx=0
        tracker={0:1}
        for i in nums:
            sumx+=i
            if sumx-k in tracker:
                ctr+=tracker[sumx-k]
            tracker[sumx]=tracker.get(sumx,0)+1
        # print(tracker)
        return ctr