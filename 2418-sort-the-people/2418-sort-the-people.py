class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for end in range(1,len(heights)):
            if heights[end] > heights[end-1]:
                start = end
                while(heights[start] > heights[start-1]):
                    heights[start], heights[start-1] = heights[start-1], heights[start]
                    names[start], names[start-1] = names[start-1], names[start]
                    start -= 1
                    if start <= 0:
                        break
        return names
                    