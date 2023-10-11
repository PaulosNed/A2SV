class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        pos = [0, 0]
        direction = (0, 1)
        
        left_shifts = {(0, 1) : (-1, 0), (-1, 0) : (0, -1), (0, -1) : (1, 0), (1, 0): (0, 1)}
        right_shifts = {(0, 1): (1, 0), (1, 0) : (0, -1), (0, -1) : (-1, 0), (-1, 0) : (0, 1)}
        
        for _ in range(4):
            
            for ins in instructions:
                if ins == "G":
                    pos[0] += direction[0]
                    pos[1] += direction[1]
                
                elif ins == "L":
                    direction = left_shifts[direction]
                    
                elif ins == "R":
                    direction = right_shifts[direction]
                    
            if pos == [0, 0]:
                return True
        
        return False
            