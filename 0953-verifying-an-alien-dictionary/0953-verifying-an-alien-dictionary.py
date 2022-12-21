class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        allWords = {}
        for i, v in enumerate(order):
            allWords[v] = i
        if len(words) < 2:
            return True
        start = 1
        while(start < len(words)):
            inner = 0
            while(words[start-1][inner] == words[start][inner]):
                if inner + 1 == len(words[start-1]) or inner + 1 == len(words[start]):
                    break
                else:
                    inner += 1
            if words[start-1][inner] != words[start][inner]:
                if allWords[words[start-1][inner]] < allWords[words[start][inner]]:
                    start += 1
                    continue
                else:
                    return False
            else:
                if inner + 1 == len(words[start-1]):
                    start += 1
                    continue
                else:
                    return False
        return True
            