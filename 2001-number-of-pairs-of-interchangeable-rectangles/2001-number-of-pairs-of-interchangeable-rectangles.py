class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        c = collections.Counter()
        for x, y in rectangles:
            gcd = math.gcd(x, y)
            c[(x // gcd, y // gcd)] += 1
        
        res = 0
        for k, v in c.items():
            res += v * (v - 1) // 2
        return res