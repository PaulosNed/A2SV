class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        first = 0
        second = 0
        nums1Copy = nums1[:m]
        i = 0
        while(first < m and second < n):
            if nums1Copy[first] <= nums2[second]:
                nums1[i] = nums1Copy[first]
                first += 1
            else:
                nums1[i] = nums2[second]
                second += 1
            i+=1
        if (second != n):
            for i in range(m+second,m+n):
                nums1[i] = nums2[second]
                second+=1
        elif (first != m):
            for i in range(n+first,m+n):
                nums1[i] = nums1Copy[first]
                first+=1
        
            
                