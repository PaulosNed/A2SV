class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        ans = []
        for j in range(len(matrix[0])):
            row = []
            for i in range(len(matrix)-1, -1, -1):
                row.append(matrix[i][j])
            ans.append(row)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = ans[i][j]