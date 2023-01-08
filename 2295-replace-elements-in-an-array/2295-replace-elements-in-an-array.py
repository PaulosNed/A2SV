class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        numbers = {}
        final = []
        for idx, num in enumerate(nums):
            numbers[num] = idx
        for op in operations:
            idx = numbers.pop(op[0])
            numbers[op[1]] = idx
        numbers = dict(sorted(numbers.items(), key=lambda x:x[1]))
        return list(numbers.keys())
        