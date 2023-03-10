class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        citations.reverse()
        
        for i, v in enumerate(citations):
            if i >= v:
                return i
        
        return len(citations)