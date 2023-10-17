class RandomizedSet:

    def __init__(self):
        self.randomSet = set()

    def insert(self, val: int) -> bool:
        if val in self.randomSet:
            return False
        
        self.randomSet.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.randomSet:
            return False
        
        self.randomSet.remove(val)
        return True

    def getRandom(self) -> int:
        currList = list(self.randomSet)
        idx = random.randint(0, len(currList) - 1)
        
        return currList[idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()