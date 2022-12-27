class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        allDomains = {}
        for domain in cpdomains:
            domain = domain.split(" ")
            subDoms = domain[1].split(".")
            i = len(subDoms) - 1
            curr = subDoms[i]
            while i >= 0:
                allDomains[curr] = allDomains.get(curr, 0) + int(domain[0])
                i -= 1
                if i < 0:
                    break
                curr = subDoms[i] + "." + curr
        final = []
        for item in allDomains:
            final.append("".join(str(allDomains[item]) + " "+ item))
        return final