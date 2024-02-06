class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ans = defaultdict(list)
        
        for s in strs:
            li_s = list(s)
            li_s.sort()
            
            
            ans["".join(li_s)].append(s)
        
        return ans.values()