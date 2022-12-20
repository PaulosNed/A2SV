class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        base = Counter(s)
        added = Counter(t)
        for item in added:
            if item not in base:
                return item
            if base[item] != added[item]:
                return item
        