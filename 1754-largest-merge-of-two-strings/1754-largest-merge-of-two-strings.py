class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        first = 0
        second = 0
        ans = ""
        while(first < len(word1) and second < len(word2)):
            if word1[first] > word2[second]:
                ans += word1[first]
                first += 1
            elif word1[first] < word2[second]:
                ans += word2[second]
                second += 1
            else:
                curr1 = word1[first]
                curr2 = word2[second]
                currFirst = first
                currSecond = second
                currFirst += 1
                currSecond += 1
                while(curr1 == curr2 and currFirst < len(word1) and currSecond < len(word2)):
                    curr1 += word1[currFirst]
                    curr2 += word2[currSecond]
                    currFirst += 1
                    currSecond += 1
                if curr2 > curr1:
                    ans += word2[second]
                    second += 1
                elif curr1 > curr2:
                    ans += word1[first]
                    first += 1
                else:
                    if currFirst >= len(word1):
                        ans += word2[second]
                        second += 1
                    else:
                        ans += word1[first]
                        first += 1
        ans += "".join(word1[first:])
        ans += "".join(word2[second:])
        return ans