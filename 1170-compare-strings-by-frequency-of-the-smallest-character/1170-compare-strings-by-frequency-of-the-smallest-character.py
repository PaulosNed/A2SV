class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        countQueries = []
        for query in queries:
            curr = Counter(query)
            countQueries.append(curr[min(curr)])
        
        countWords = []
        for word in words:
            curr = Counter(word)
            countWords.append(curr[min(curr)])
        countWords.sort()
            
        ans = []
        for target in countQueries:
            left = 0
            right = len(countWords) - 1
            while(left <= right):
                mid = left + ((right - left) // 2)
                if countWords[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            ans.append(len(countWords[left:]))
        return ans
        