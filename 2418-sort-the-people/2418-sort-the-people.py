class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for _ in range(len(heights)):
            for i in range(1,len(heights)):
                if heights[i-1] < heights[i]:
                    heights[i-1], heights[i] = heights[i], heights[i-1]
                    names[i-1], names[i] = names[i], names[i-1]
        return names
                