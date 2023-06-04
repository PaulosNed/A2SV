class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        queue = [0]
        
        while(queue):
            curr = queue.pop(0)
            
            if curr in visited:
                continue
                
            visited.add(curr)
            queue.extend(rooms[curr])
        
        return len(visited) == len(rooms)
            