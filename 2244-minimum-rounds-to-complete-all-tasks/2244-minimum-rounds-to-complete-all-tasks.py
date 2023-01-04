class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        countTasks = Counter(tasks)
        rounds = 0
        for task in countTasks:
            while(countTasks[task] > 3):
                if countTasks[task] == 4:
                    rounds+=2
                    countTasks[task] = 0
                    break
                rounds += 1
                countTasks[task] -= 3
            if countTasks[task] == 1:
                return -1
            elif countTasks[task] == 0:
                continue
            else:
                rounds += 1
        return rounds