class Solution(object):
    def findAnagrams(self, s, p):
        start = 0
        end = len(p)-1
        ans = []
        countWord = Counter(s[start:end+1])
        countP = Counter(p)
        while(end < len(s)):
            if countWord == countP:
                ans.append(start)
            countWord[s[start]] -= 1
            if countWord[s[start]] == 0:
                countWord.pop(s[start])
            start += 1
            end += 1
            if end < len(s):
                countWord[s[end]] = countWord.get(s[end], 0) + 1
        return ans
                