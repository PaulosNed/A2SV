class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if len(mat) <= 1:
            return mat[0]
        if len(mat[0]) <= 1:
            ans = []
            for item in mat:
                ans.append(item[0])
            return ans
        i = 0
        j = 1
        ordered = [mat[0][0]]
        fromJLI = False
        fromILJ = True
        while(i != len(mat)-1 or j != len(mat[0]) - 1):
            if fromILJ:
                fromILJ = False
                fromJLI = True    
                while True:
                    ordered.append(mat[i][j])
                    if i+1 < len(mat):
                        i+=1
                        if j - 1 < 0:
                            break
                        j-=1
                    else:
                        if j + 1 < len(mat[0]):
                            j+=1
                        break
            elif fromJLI:
                fromILJ = True
                fromJLI = False
                while True:
                    ordered.append(mat[i][j])
                    if j+1 < len(mat[0]):
                        j+=1
                        if i-1 < 0:
                            break
                        i-=1
                    else:
                        if i+1 < len(mat):
                            i+=1
                        break
        ordered.append(mat[-1][-1])
        return ordered
        