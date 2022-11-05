class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorter = {}
        tempInterval = []
        for item in intervals:
            if item[0] in sorter:
                sorter[item[0]] = item[1] if item[1] > sorter[item[0]] else sorter[item[0]]
            else:
                sorter[item[0]] = item[1]
        for i in sorted(sorter):
            tempInterval.append([i, sorter[i]])
        intervals = tempInterval
        i = 1
        print(intervals)
        while(i < len(intervals)):
            if intervals[i][0] <= intervals[i-1][1]:
                b = max(intervals[i][1], intervals[i-1][1])
                temp = [intervals[i-1][0], b]
                intervals.pop(i)
                intervals.pop(i-1)
                intervals.insert(i-1, temp)
            else:
                i+=1
        return intervals