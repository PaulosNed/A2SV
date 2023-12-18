class ATM:

    def __init__(self):
        self.tracker = [0] * 5
        self.notes = {0: 20, 1: 50, 2: 100, 3: 200, 4: 500}

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.tracker[i] += banknotesCount[i]
        

    def withdraw(self, amount: int) -> List[int]:
        withdrawen = [0] * 5
        
        for i in range(4, -1, -1):
            if self.tracker[i]:
                curr = amount // self.notes[i]
                
                amount -= min(curr, self.tracker[i]) * self.notes[i]
                withdrawen[i] += min(curr, self.tracker[i])
        
        if amount:
            return [-1]
        
        for i in range(5):
            self.tracker[i] -= withdrawen[i]
        
        return withdrawen
        
        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)