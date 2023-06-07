class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:

        @cache
        def dp(idx):
            if idx >= len(questions):
                return 0

            opt1 = dp(idx+1)
            opt2 = questions[idx][0] + dp(idx + questions[idx][1] + 1)

            return max(opt1, opt2)
        
        return dp(0)