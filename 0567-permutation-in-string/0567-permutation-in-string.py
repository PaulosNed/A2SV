class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        countS1 = Counter(s1)
        start = 0
        end = len(s1) - 1
        countS2 = Counter(s2[start:end+1])
        while(end < len(s2)):
            if countS1 == countS2:
                return True
            countS2[s2[start]] -= 1
            if countS2[s2[start]] == 0:
                countS2.pop(s2[start])
            start += 1
            end += 1
            if end < len(s2):
                countS2[s2[end]] = countS2.get(s2[end], 0) + 1
            