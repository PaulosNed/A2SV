class Solution:
    def pivotInteger(self, n: int) -> int:
        
        ps = [1]
        for i in range(2, n + 1):
            ps.append(ps[-1] + i)
        
        ps_reversed = [i for i in range(1, n + 1)]
        for i in range(len(ps_reversed) - 2, -1, -1):
            ps_reversed[i] += ps_reversed[i + 1]
        
        for i in range(n):
            if ps[i] == ps_reversed[i]:
                return i + 1
        
        return -1