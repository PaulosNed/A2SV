class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        first = [i + values[i] for i in range(len(values))]
        second = [values[j] - j for j in range(len(values))]
        tracker = []
        for i, v in enumerate(second):
            tracker.append((v, i))
        
        tracker.sort()
        
        i = 0
        j = 0
        ans = float('-inf')
        while i < len(values) - 1:
            
            while(j <= i):
                val, idx = tracker.pop()
                if idx > i:
                    j = idx
                    break
            
            ans = max(ans, first[i] + second[j])
            i += 1
        
        return ans
            
            
                        