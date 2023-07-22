class TupleWrapper:
    def __init__(self, tuple):
        self.tuple = tuple

    def __lt__(self, other):
        if self.tuple[0] < other.tuple[0]:
            return True
        elif self.tuple[0] == other.tuple[0]:
            return self.tuple[2] < other.tuple[2]
        else:
            return False

    def __getitem__(self, index):
        return self.tuple[index]


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        for i in range(len(tasks)):
            tasks[i].append(i)
        
        tasks.sort()
        ans = []
        
        j = 0
        sorterHeap = []
        
        while j < len(tasks) and tasks[j][0] <= tasks[0][0]:
            start, time, idx = tasks[j]
            heappush(sorterHeap, TupleWrapper((time, start, idx)))
            j += 1
        
        globalTime = sorterHeap[0][1]
        while sorterHeap:
            time, start, idx = heappop(sorterHeap)
            ans.append(idx)
            globalTime += time
            
            while j < len(tasks) and tasks[j][0] <= globalTime:
                heappush(sorterHeap, TupleWrapper((tasks[j][1], tasks[j][0], tasks[j][2])))
                j += 1
            
            if not sorterHeap and j < len(tasks):
                heappush(sorterHeap, TupleWrapper((tasks[j][1], tasks[j][0], tasks[j][2])))
                globalTime = tasks[j][0]
                j += 1

            
        return ans
            
                