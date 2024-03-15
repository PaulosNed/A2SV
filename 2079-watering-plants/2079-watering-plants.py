class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        
        steps = 0
        curr = capacity
        
        for i, val in enumerate(plants):
            if val <= curr:
                curr -= val
            
            else:
                steps += (2 * (i))
                curr = capacity - val
        
            steps += 1
            
        return steps