class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(heights)):
            minVal = 0
            idx = None
            for j in range(i, len(heights)):
                if heights[j] > minVal:
                    minVal = heights[j]
                    idx = j
            heights[i], heights[idx] = heights[idx], heights[i]
            names[i], names[idx] = names[idx], names[i]
        return names