class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ops = 0
        for log in logs:
            if log == "../":
                ops -= 1
                if ops < 0:
                    ops = 0
            elif log == "./":
                continue
            else:
                ops += 1
        return ops