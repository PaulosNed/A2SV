class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        checker = []
        for row in mat:
            checker.extend(row)
        if len(checker) != r*c:
            return mat
        ans = []
        r = []
        initialC = c
        for i in range(len(checker)):
            if i == c:
                ans.append(r)
                r = [checker[i]]
                c += initialC
            else:
                r.append(checker[i])
        ans.append(r)
        return ans