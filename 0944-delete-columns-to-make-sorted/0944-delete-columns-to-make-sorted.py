class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        columns = 0
        tracer = defaultdict(list)
        for s in strs:
            i = 0
            while(i<len(s)):
                tracer[i].append(s[i])
                i += 1
        for i in tracer:
            j = 1
            while(j < len(tracer[i])):
                if tracer[i][j-1] > tracer[i][j]:
                    columns += 1
                    break
                j += 1
        return columns