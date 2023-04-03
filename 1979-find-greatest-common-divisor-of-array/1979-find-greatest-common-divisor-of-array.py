class Solution:
    def findGCD(self, nums: List[int]) -> int:
        return self.GCD(max(nums), min(nums))
        
    def GCD(self, num1, num2):
        if not num1:
            return num2
        if not num2:
            return num1
        
        return self.GCD(num2, num1 % num2)