class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        length = x // 2
        low = 1
        high = length
        while(low <= high):
            mid = low + ((high - low) // 2)
            if mid ** 2 > x:
                high = mid - 1
            elif mid ** 2 < x and (mid + 1) ** 2 <= x:
                low = mid + 1
            else:
                return mid