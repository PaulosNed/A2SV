class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        while(matrix):
            ans.extend(matrix[0][:-1])
            idx = 0
            while(idx < len(matrix)):
                ans.append(matrix[idx][-1])
                matrix[idx].pop()
                if not matrix[idx]:
                    matrix.pop(idx)
                else:
                    idx += 1
            if not matrix:
                break
            matrix.pop(0)
            if not matrix:
                break
            ans.extend(reversed(matrix[-1]))
            idx = len(matrix)-2
            while idx >= 0:
                ans.append(matrix[idx][0])
                matrix[idx].pop(0)
                if not matrix[idx]:
                    matrix.pop(idx)
                idx -= 1
            if not matrix:
                break
            matrix.pop()
            if not matrix:
                break
        return ans