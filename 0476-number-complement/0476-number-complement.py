class Solution:
    def findComplement(self, num: int) -> int:
        length = num.bit_length()
        op = 2**length - 1
        return num^op