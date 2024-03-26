class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        swaps = 0
        n = len(row)
        
        for i in range(0, n, 2):
            
            if row[i] % 2 == 0:
                if row[i + 1] == row[i] + 1:
                    continue
                    
                for j in range(i, len(row)):
                    if row[j] == row[i] + 1:
                        row[j], row[i + 1] = row[i + 1], row[j]
                        
            else:
                
                if row[i + 1] == row[i] - 1:
                    continue
                    
                for j in range(i, len(row)):
                    if row[j] == row[i] - 1:
                        row[j], row[i + 1] = row[i + 1], row[j]
                        
            
            swaps += 1
        
        return swaps