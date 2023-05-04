class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue = deque([(entrance[0],entrance[1])])
        directions = [(0,-1), (0,1), (-1,0), (1,0)]
        count = 0
        visited = {(entrance[0],entrance[1])}
        while queue:
            size = len(queue)
            for _ in range(size):
                curr = queue.popleft()
                if curr[0] == 0 or curr[0] == len(maze) - 1 or curr[1] == 0 or curr[1] ==  len(maze[0]) -1:
                    if list(curr) != entrance:
                        return count
                for direction in directions:
                    nxt = (curr[0]-direction[0], curr[1]-direction[1])
                    if 0 <= nxt[0] < len(maze) and 0 <= nxt[1] < len(maze[0]) and nxt not in visited and maze[nxt[0]][nxt[1]] != '+':
                        queue.append(nxt)   
                        visited.add(nxt)
            
            count += 1
        
        return -1