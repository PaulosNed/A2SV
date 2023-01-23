class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n==1:
            return 1
        allTrustee = {}
        allTrusted = {}
        for trustee, trusted in trust:
            if trustee not in allTrustee:
                allTrustee[trustee] = set()
            if trusted not in allTrusted:
                allTrusted[trusted] = set()
            allTrustee[trustee].add(trusted)
            allTrusted[trusted].add(trustee)
        for p in range(1,n+1):
            if p not in allTrustee:
                exceptPerson = set([i for i in range(1,n+1)])
                exceptPerson.remove(p)
                if p not in allTrusted:
                    continue
                if allTrusted[p] == exceptPerson:
                    return p
        return -1