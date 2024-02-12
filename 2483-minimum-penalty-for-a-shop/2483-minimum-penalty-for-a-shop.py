class Solution:
    def bestClosingTime(self, customers: str) -> int:
        
        rs = 0
        max_sum = 0
        idx = 0
        
        for i, val in enumerate(customers):
            if val == "Y":
                rs += 1
            
            else:
                if rs > max_sum:
                    max_sum = rs
                    idx = i
                
                rs -= 1
        
        if rs > max_sum:
            return len(customers)
                
        return idx
                    