class Solution:
    def __init__(self):
        self.count = 0
        
    def reversePairs(self, nums: List[int]) -> int:
        self.mergeSort(0, len(nums)-1, nums)
        return self.count
    
    def merge(self, nums1: List[int], nums2: List[int]) -> None:
        first = 0
        second = 0
        while(first < len(nums1) and second < len(nums2)):
            if nums1[first] > nums2[second] * 2:
                self.count += len(nums1) - first
                second += 1
            else:
                first += 1
        
        first = 0
        second = 0
        ans = []
        while(first < len(nums1) and second < len(nums2)):
            if nums1[first] <= nums2[second]:
                ans.append(nums1[first])
                first += 1
            else:
                ans.append(nums2[second])
                second += 1
                
        ans.extend(nums2[second:])
        ans.extend(nums1[first:])
        return ans
                
    def mergeSort(self, left, right, arr):
        if left == right:
            return [arr[left]]
        mid = left + (right - left) // 2
        left_half = self.mergeSort(left, mid, arr)
        right_half = self.mergeSort(mid + 1, right, arr)

        return self.merge(left_half, right_half)
