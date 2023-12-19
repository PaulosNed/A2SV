class Solution:
    
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        
        directions = [(0, -1), (-1, -1), (1, -1), (-1, 0), (1, 1), (0, 1), (-1, 1), (1, 0)]
        
        def isBound(r, c):
            # print(r, c)
            if 0 <= r < len(img) and 0 <= c < len(img[0]):
                return True
            
            return False

        def findSum(i, j):
            
            sum_ = img[i][j]
            cnt = 1

            for r, c in directions:
                nr, nc = i + r, j + c

                if isBound(nr, nc):
                    sum_ += img[nr][nc]
                    cnt += 1
            
            return floor(sum_ / cnt)
        
        ans = [[0 for i in range(len(img[0]))] for i in range(len(img))]
        for i in range(len(img)):
            for j in range(len(img[0])):
                ans[i][j] = findSum(i, j)
        
        return ans
