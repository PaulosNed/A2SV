class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        num1 = int(math.sqrt(c))
        while(num1 >= 0):
            curr = math.sqrt(c - num1**2)
            if curr.is_integer():
                return True
            num1 -= 1
        return False