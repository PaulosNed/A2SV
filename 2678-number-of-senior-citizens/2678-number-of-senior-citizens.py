class Solution:
    def countSeniors(self, details: List[str]) -> int:
        
        cnt = 0
        for detail in details:
            if int(detail[-4:-2]) > 60:
                cnt += 1
        
        return cnt