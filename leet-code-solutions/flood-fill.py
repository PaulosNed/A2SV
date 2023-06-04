class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        stack = [(sr, sc)]
        directions = [(0,-1), (0,1), (-1,0), (1,0)]
        initial = image[sr][sc]
        if initial == color:
            return image
        
        while stack:
            curr = stack.pop()
            if 0 <= curr[0] < len(image) and 0 <= curr[1] < len(image[0]):
                if image[curr[0]][curr[1]] != initial:
                    continue

                image[curr[0]][curr[1]] = color
                for direction in directions:
                    stack.append(((curr[0]  + direction[0]), (curr[1]  + direction[1])))
            
        return image
            