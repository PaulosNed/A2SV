class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque()
        for i, v in enumerate(tickets):
            queue.append([i,v])
        total_time = 0
        while True:
            curr = queue.popleft()
            curr[1] -= 1
            total_time += 1
            if curr[1] != 0:
                queue.append(curr)
            elif curr[0] == k:
                return total_time
        