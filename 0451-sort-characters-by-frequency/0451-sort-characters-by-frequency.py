class Solution:
    def frequencySort(self, s: str) -> str:
        
        count = Counter(s)
        ans = []
        
        for key in count:
            ans.append((count[key], key))
        
        ans.sort(reverse=True)
        
        final = ""
        
        for char, frq in ans:
            final += (char * frq)
        
        return final