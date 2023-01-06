class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        ans = ""
        num1 = num1.split("+")
        num2 = num2.split("+")
        firstPart = int(num1[0])*int(num2[0])
        firstPart += (int(num1[1][:-1])*int(num2[1][:-1])*-1)
        firstPart = str(firstPart)
        firstPart += "+"
        secondPart = int(num1[0])*int(num2[1][:-1])
        secondPart += int(num2[0])*int(num1[1][:-1])
        secondPart = str(secondPart) + "i"
        return firstPart + secondPart