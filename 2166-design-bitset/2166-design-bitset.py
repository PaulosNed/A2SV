class Bitset:

    def __init__(self, size: int):
        self.bits = "0" * size
        self.flipped = False
        self.cnt = 0

    def fix(self, idx: int) -> None:
        
        if self.flipped and self.bits[idx] == "1":
            self.cnt += 1
            self.bits = self.bits[:idx] + "0" + self.bits[idx+1:]
        
        elif not self.flipped and self.bits[idx] == "0":
            self.cnt += 1
            self.bits = self.bits[:idx] + "1" + self.bits[idx+1:]

    def unfix(self, idx: int) -> None:
        
        if self.flipped and self.bits[idx] == "0":
            self.cnt -= 1
            self.bits = self.bits[:idx] + "1" + self.bits[idx+1:]
        
        elif not self.flipped and self.bits[idx] == "1":
            self.cnt -= 1
            self.bits = self.bits[:idx] + "0" + self.bits[idx+1:]

    def flip(self) -> None:
        self.flipped = not self.flipped
        self.cnt = len(self.bits) - self.cnt
        
    def all(self) -> bool:
        return self.cnt == len(self.bits)
        
    def one(self) -> bool:
        return self.cnt > 0

    def count(self) -> int:
        return self.cnt

    def toString(self) -> str:
        if self.flipped:
            ans = ""
            
            for s in self.bits:
                ans += "0" if s == "1" else "1"
            
            return ans
        return self.bits


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()