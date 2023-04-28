class LockingTree:

    def __init__(self, parent: List[int]):
        self.parents = parent
        self.locks = [-1] * len(parent)
        self.graph = defaultdict(list)
        for i, p in enumerate(self.parents):
            if p == -1:
                continue
            
            self.graph[p].append(i)

    def lock(self, num: int, user: int) -> bool:
        if self.locks[num] != -1:
            return False
        
        self.locks[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if self.locks[num] == user:
            self.locks[num] = -1
            return True
        return False

    def upgrade(self, num: int, user: int) -> bool:
        curr = num
        while(curr != -1):
            if self.locks[curr] != -1:
                return False
            curr = self.parents[curr]
            
        queue = deque([num])
        flag = False
        while(queue):
            curr = queue.popleft()
            if self.locks[curr] != -1:
                flag = True
                self.locks[curr] = -1
            
            for child in self.graph[curr]:
                queue.append(child)
                    
        if flag:
            self.locks[num] = user
        
        return flag
                


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)