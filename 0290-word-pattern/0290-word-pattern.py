class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        patternTracker = {}
        if len(pattern) != len(s):
            return False
        for idx,letter in enumerate(pattern):
            if letter not in patternTracker:
                if s[idx] in patternTracker.values():
                    return False
                patternTracker[letter] = s[idx]
                continue
            else:
                if patternTracker[letter] != s[idx]:
                    return False
        return True