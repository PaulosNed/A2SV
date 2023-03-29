class Solution:
    def countBits(self, n: int) -> List[int]:
        list2=[0]*(n+1)
        for i in range(n+1):
            x=list(bin(i)[2:])
            z=x.count('1')
            list2.append(z)
        return list2[n+1:]