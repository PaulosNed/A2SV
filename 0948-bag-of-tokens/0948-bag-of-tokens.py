class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score = 0
        start = 0
        end = len(tokens) - 1
        while(start < end):
            if power >= tokens[start]:
                power-=tokens[start]
                score+=1
                start+=1
            else:
                if score >= 1:
                    score-=1
                    power+=tokens[end]
                    end-=1
                else:
                    return score
        if start == end:
            if power >= tokens[start]:
                score += 1
        return score
                    