class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        
        filled = defaultdict(int)
        filled[(0,0)] = poured
        for i in range(1, query_row + 1):
            for j in range(i+1):
                extra = max(0, (filled[(i-1, j-1)] - 1) / 2) + max(0, (filled[(i-1, j)] - 1)/2)
                filled[(i,j)] = extra
        
        return min(1, filled[(query_row, query_glass)])