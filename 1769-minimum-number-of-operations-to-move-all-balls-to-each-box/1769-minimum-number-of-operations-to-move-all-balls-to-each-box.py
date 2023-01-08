class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        if len(boxes) < 2:
            return [0]
        start = 0
        end = 1
        ans = []
        for i in range(len(boxes)):
            curr = 0
            for j in range(len(boxes)):
                if i == j:
                    continue
                if boxes[j] == "1":
                    curr += abs(j-i)
            ans.append(curr)
        return ans
                    