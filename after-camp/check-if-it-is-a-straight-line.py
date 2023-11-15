class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        m = None
        first = True
        
        for i in range (1, len(coordinates)):
            x1, y1 = coordinates[i]
            x2, y2 = coordinates[i-1]
            
            if first:
                first = False
                m = (x1 - x2) / (y1 - y2) if y1 - y2 != 0 else float('inf') 
            
            else:
                curr = (x1 - x2) / (y1 - y2) if y1 - y2 != 0 else float('inf')
                if m != curr:
                    return False
        
        return True
            