class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort(reverse = True)
        tasks.sort()
        
        max_time = 0
        
        i = 0
        j = 3
        
        while i < len(processorTime):
            max_time = max(max_time, processorTime[i] + tasks[j])
            i += 1
            j += 4
        
        return max_time