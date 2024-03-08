class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        
        def recurse(currRow):
            if currRow <= 0:
                return
            
            if len(ans) == 0:
                ans.append([1])
            
            elif len(ans) == 1:
                ans.append([1,1])
            
            else:
                currAns = [1]
                for i in range(1, len(ans[-1])):
                    currAns.append(ans[-1][i] + ans[-1][i - 1])
                currAns.append(1)
                ans.append(currAns)
            
            recurse(currRow - 1)
        
        recurse(numRows)
        return ans