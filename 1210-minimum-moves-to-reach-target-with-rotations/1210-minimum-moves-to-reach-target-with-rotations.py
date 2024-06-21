class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dq = collections.deque([((0, 0, 0, 1), 0)])
        visited = set()
        
        while dq:
            
            (tail_r, tail_c, head_r, head_c), step = dq.popleft()
            
            if (tail_r, tail_c, head_r, head_c) in visited: 
                continue
            
            if (tail_r, tail_c) == (n - 1, n - 2) and (head_r, head_c) == (n - 1, n - 1): 
                return step
            
            visited.add((tail_r, tail_c, head_r, head_c))
            if head_c + 1 < n and grid[tail_r][tail_c + 1] != 1 and grid[head_r][head_c + 1] != 1: 
                dq.append(((tail_r, tail_c + 1, head_r, head_c + 1), step + 1)) # move right
            
            if head_r + 1 < n and grid[tail_r + 1][tail_c] != 1 and grid[head_r + 1][head_c] != 1: 
                dq.append(((tail_r + 1, tail_c, head_r + 1, head_c), step + 1)) # move down
            
            if tail_r == head_r and head_r + 1 < n and grid[tail_r + 1][tail_c] != 1 and grid[head_r + 1][head_c] != 1: 
                dq.append(((tail_r, tail_c, head_r + 1, head_c - 1), step + 1)) # rotate clockwise
            
            if tail_c == head_c and head_c + 1 < n and grid[tail_r][tail_c + 1] != 1 and grid[head_r][head_c + 1] != 1: 
                dq.append(((tail_r, tail_c, head_r - 1, head_c + 1), step + 1)) # rotate counter clockwise
                
                
        return -1