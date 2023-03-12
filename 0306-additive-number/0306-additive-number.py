class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        curr = []
        
        if len(num) <= 2:
            return False
        
        def backtrack(start, end):
            if end >= len(num):
                return len(curr) > 2
            
            while end < len(num):
                if len(curr) < 2 or curr[-1] + curr[-2] == int(num[start : end+1]):
                    if start != end and int(num[start]) == 0:
                        if not curr:
                            return False
                        curr[-1] = int(str(curr[-1]) + "0")
                        end += 1
                        continue
                    curr.append(int(num[start : end+1]))
                    if backtrack(end+1, end+1):
                        return True
                    curr.pop()
                
                end += 1
        
        return backtrack(0,0)