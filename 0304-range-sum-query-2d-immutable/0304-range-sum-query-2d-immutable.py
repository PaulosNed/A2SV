class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.arr=[[0]*len(matrix[0]) for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.arr[i][j]=self.arr[i][j-1]+matrix[i][j]
        for i in range(1,len(matrix)):
            for j in range(len(matrix[0])):
                self.arr[i][j]+=self.arr[i-1][j]
        
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        main=self.arr[row2][col2]
        sub_1=self.arr[row1-1][col2] if row1-1>-1 else 0
        sub_2=self.arr[row2][col1-1] if col1-1>-1 else 0
        overlap=self.arr[row1-1][col1-1] if row1-1>-1 and col1-1>-1 else 0
        return main-sub_1-sub_2+overlap
        

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)