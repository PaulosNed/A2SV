class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        x=list(range(1,n+1))
        stack=[]
        seen=[]
        for i in range(len(x)):
            if seen==target:
                return stack
            if x[i] in target:
                stack.append('Push')
                seen.append(x[i])
            else:
                stack.append('Push')
                stack.append('Pop')
        return stack