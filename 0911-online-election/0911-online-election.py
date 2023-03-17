class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.leading = [0] * (len(self.times))
        first = min(self.persons)
        last = max(self.persons)
        count = [0] * (last - first + 1)
        currMax = 0
        for i in range(len(self.persons)):
            if count[self.persons[i] - first] + 1 >= count[currMax]:
                currMax = self.persons[i]
            self.leading[i] = currMax
            count[self.persons[i] - first] += 1
            
    def q(self, t: int) -> int:
        start = 0
        end = len(self.times) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if self.times[mid] > t:
                end = mid - 1
            elif self.times[mid] < t:
                start = mid + 1
            else:
                return self.leading[mid]
        return self.leading[start-1]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)