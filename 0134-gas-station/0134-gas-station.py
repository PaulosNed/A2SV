class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        length = len(gas)
        gas += gas
        cost += cost
        initial = 0
        idx = -1
        for i in range(len(gas)-1):
            curr = initial + gas[i] - cost[i]
            if curr >= 0:
                initial = curr
                if idx == -1:
                    idx = i
            else:
                initial = 0
                idx = -1
        if idx > length:
            return -1
        return idx