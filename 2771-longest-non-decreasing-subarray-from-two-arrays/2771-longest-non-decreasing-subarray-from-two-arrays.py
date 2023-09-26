class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        
        option1 = [1] * len(nums1)
        option2 = [1] * len(nums2)
        
        for i in range(len(nums1) - 2, -1, -1):
            
            
            # for nums1
            if nums1[i] <= nums1[i + 1]:
                option1[i] = max(option1[i], 1 + option1[i + 1])
            
            if nums1[i] <= nums2[i + 1]:
                option1[i] = max(option1[i], 1 + option2[i + 1])
            
            
            # for nums2
            if nums2[i] <= nums1[i + 1]:
                option2[i] = max(option2[i], 1 + option1[i + 1])
                
            if nums2[i] <= nums2[i + 1]:
                option2[i] = max(option2[i], 1 + option2[i + 1])
        
        return max(option1 + option2)
                
            