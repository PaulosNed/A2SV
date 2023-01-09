class DataStream:

    def __init__(self, value: int, k: int):
        self.stream = []
        self.checker = defaultdict(int)
        self.value = value
        self.k = k

    def consec(self, num: int) -> bool:
        if len(self.stream) == self.k:
            item = self.stream.pop(0)
            self.checker[item] -= 1
            if self.checker[item] == 0:
                self.checker.pop(item)
        self.stream.append(num)
        self.checker[num] += 1
        if len(self.stream) < self.k:
            return False 
        if len(self.checker) == 1:
            if self.value in self.checker:
                return True
            else:
                return False


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)