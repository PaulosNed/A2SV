class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        changes = {5:0, 10:0, 20:0}
        
        for bill in bills:
            if bill == 10:
                if not changes[5]:
                    return False
                changes[5] -= 1
            
            elif bill == 20:
                if changes[10] >= 1 and changes[5] >= 1:
                    changes[10] -= 1
                    changes[5] -= 1
                    
                elif changes[5] >= 3:
                    changes[5] -= 3
                
                else:
                    return False
                    
            changes[bill] += 1
        
        return True