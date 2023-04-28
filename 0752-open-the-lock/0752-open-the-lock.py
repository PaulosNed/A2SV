class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = deque(['0000'])
        visited = {'0000'}
        deadends =set(deadends)
        count = 0
        if '0000' in deadends:
            return -1
        
        while(queue):
            size = len(queue)
            
            for _ in range(size):
                curr = queue.popleft()
                if curr == target:
                    return count
                neighbours = self.getNeighbours(list(curr))
                
                for neighbour in neighbours:
                    if neighbour not in visited and neighbour not in deadends:
                        queue.append(neighbour)
                        visited.add(neighbour)
                        
            count += 1
        
        return -1
        
        
        
        
    def getNeighbours(self, curr):
        neighbours = []
        for i in range(len(curr)):
            temp = curr[:]
            if temp[i] == '0':
                temp[i] = '9'
                neighbours.append(''.join(temp))
                temp[i] = '1'
                neighbours.append(''.join(temp))
            
            elif temp[i] == '9':
                temp[i] = '0'
                neighbours.append(''.join(temp))
                temp[i] = '8'
                neighbours.append(''.join(temp))
                
            else:
                temp[i] = str(int(curr[i]) + 1)
                neighbours.append(''.join(temp))
                temp[i] = str(int(curr[i]) - 1)
                neighbours.append(''.join(temp))
        
        return neighbours
                    