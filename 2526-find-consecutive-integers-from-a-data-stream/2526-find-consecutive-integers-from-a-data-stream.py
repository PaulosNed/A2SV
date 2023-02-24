class DataStream:

    def __init__(self, value: int, k: int):
        self.stream = deque()
        self.count = 0
        self.value = value
        self.k = k

    def consec(self, num: int) -> bool:
        if len(self.stream) == self.k:
            popped = self.stream.popleft()
            if self.count > 0 and popped == self.value:
                self.count -= 1
        self.stream.append(num)
        if num == self.value:
            self.count += 1
        else:
            self.count = 0
        if self.count == self.k:
            return True
        return False
        

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)