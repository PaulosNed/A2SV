class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        exist = set()
        ans = 0
        while(end < len(s)):
            if s[end] not in exist:
                exist.add(s[end])
                end += 1
            else:
                ans = max(ans, end-start)
                exist.remove(s[start])
                start += 1
        ans = max(ans, end-start)
        return ans