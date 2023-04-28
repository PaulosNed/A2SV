class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ans = [[0] * len(mat[0]) for _ in range(len(mat))]
        queue = deque([])
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if not mat[r][c]:
                    queue.append((r, c))
                    visited.add((r,c))
        count = 0
        while queue:
            size = len(queue)
            
            for _ in range(size):
                r, c = queue.popleft()
                ans[r][c] = count
                
                for direction in directions:
                    nxt = (r - direction[0], c - direction[1])
                    if 0 <= nxt[0] < len(mat) and 0 <= nxt[1] < len(mat[0]) and nxt not in visited and mat[nxt[0]][nxt[1]] == 1:
                        queue.append(nxt)
                        visited.add(nxt)
            
            count += 1
        
        return ans
                
            
                    
        