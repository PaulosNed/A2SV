class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        ans = [-1] * len(intervals)
        max_ = max(intervals)[0]
        min_ = min(intervals)[0]
        checker = [0] * (max_ - min_ +1)
        tracker = {}
        for i, interval in enumerate(intervals):
            checker[interval[0] - min_] = 1
            tracker[interval[0]] = i
            
        intervals.sort(key = lambda x: x[1])
        
        first = 0
        second = 0
        while(first < len(intervals) and second < len(checker)):
            second = intervals[first][1] - min_
            if second >= len(checker):
                return ans
            
            while(checker[second] != 1):
                second += 1
                if second >= len(checker):
                    return ans
            
            ans[tracker[intervals[first][0]]] = tracker[second + min_]
            first += 1
            
        return ans
            