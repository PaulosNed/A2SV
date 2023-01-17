class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(heights)):
            minVal = float("inf")
            idx = None
            for j in range(i, len(heights)):
                if heights[j] < minVal:
                    print(heights[j], minVal, i)
                    minVal = heights[j]
                    idx = j
            heights[i], heights[idx] = heights[idx], heights[i]
            names[i], names[idx] = names[idx], names[i]
        names.reverse()
        return names