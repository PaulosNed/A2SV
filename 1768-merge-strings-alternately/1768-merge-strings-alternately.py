class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        length = min(len(word1), len(word2))
        for i in range(length):
                       ans += word1[i]
                       ans += word2[i]
        if len(word1) > length:
                     ans += word1[length:]
        elif len(word2) > length:
                     ans += word2[length:]
        return ans