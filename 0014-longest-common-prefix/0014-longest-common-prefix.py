class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        start = 1
        common = ""
        temp = strs[:start]
        while(True):
            for item in strs:
                if len(common) == len(item):
                    return common
                if strs[0][:start] != item[:start]:
                    return common
            common = strs[0][:start]
            start += 1