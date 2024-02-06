class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ans = [words[0]]
        
        for word in words:
            if Counter(ans[-1]) != Counter(word):
                ans.append(word)
        
        return ans
                
                