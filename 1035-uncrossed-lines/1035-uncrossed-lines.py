class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        
        @cache
        def dp(idx1, idx2):
            if idx1 >= len(nums1) or idx2 >= len(nums2):
                return 0
            
            opt1 = dp(idx1+1, idx2)
            for i in range(idx2, len(nums2)):
                if nums2[i] == nums1[idx1]:
                    opt1 = max(opt1, 1 + dp(idx1 + 1, i + 1))
            
            return opt1
        
        return dp(0, 0)
                
        