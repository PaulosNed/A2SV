class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        acc = 0
        mod = [0] * len(s)
        ans = ""
        for query in shifts:
            if query[2] == 1:
                mod[query[0]] += 1
                if query[1] + 1 < len(mod):
                    mod[query[1] + 1] -= 1
            else:
                mod[query[0]] -= 1
                if query[1] + 1 < len(mod):
                    mod[query[1] + 1] += 1
        for j in range(len(s)):
            acc += mod[j]
            currLetter = ord(s[j]) + acc 
            if currLetter > 122:
                currLetter = (currLetter - 122)%26
                if not currLetter:
                    currLetter = 26
                currLetter = 96 + currLetter
            elif currLetter < 97:
                currLetter = (97 - currLetter)%26
                if not currLetter:
                    currLetter = 26
                currLetter = 123 - currLetter
            ans += chr(currLetter)
        return ans