class Solution:
    def printVertically(self, s: str) -> List[str]:
        s= s.split(" ")
        allLetters = defaultdict(list)
        ans = []
        for i,word in enumerate(s):
            for idx,letter in enumerate(word):
                if len(allLetters[idx]) != i:
                    for j in range(i - len(allLetters[idx])):
                        allLetters[idx].append(" ")
                allLetters[idx].append(letter)
        for item in allLetters:
            ans.append("".join(allLetters[item]))
        return ans