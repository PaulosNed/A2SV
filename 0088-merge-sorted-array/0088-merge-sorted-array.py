class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        first = 0
        second = 0
        ans = []
        while(first < m and second < n):
            if nums1[first] <= nums2[second]:
                ans.append(nums1[first])
                first += 1
            else:
                ans.append(nums2[second])
                second += 1
        ans.extend(nums2[second:])
        ans.extend(nums1[first:])
        for i in range(len(nums1)):
            nums1[i] = ans[i]
            
                