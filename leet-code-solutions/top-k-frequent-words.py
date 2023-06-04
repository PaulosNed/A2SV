class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        ans = []
        while(len(ans) < k):
            max_val = max(count.values())
            for key in sorted(count):
                if count[key] == max_val:
                    ans.append(key)
                    if len(ans) == k:
                        return ans
                    count.pop(key)
        
        return ans