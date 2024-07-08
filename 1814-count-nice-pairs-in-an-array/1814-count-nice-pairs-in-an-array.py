class Solution:
    MODULO = 1_000_000_007

    def countNicePairs(self, nums: List[int]) -> int:
        
        pairs = collections.defaultdict(list)
        for n in nums:
            difference = n - int(str(n)[::-1])
            pairs[difference].append(n)

        answer = 0
        for numbers in pairs.values():
            answer += ((len(numbers) - 1) * len(numbers) // 2) % self.MODULO
        
        
        return answer % self.MODULO