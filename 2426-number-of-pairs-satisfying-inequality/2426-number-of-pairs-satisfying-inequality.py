class Solution:
    def __init__(self):
        self.valid = 0
        
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        nums = []
        for i in range(len(nums1)):
            nums.append(nums1[i] - nums2[i])
        self.mergeSort(0, len(nums)-1, nums, diff)
        return self.valid
    
    def merge(self, nums1: List[int], nums2: List[int], diff) -> None:
        first = 0
        second = 0
        while(first < len(nums1) and second < len(nums2)):
            if nums1[first] <= nums2[second] + diff:
                self.valid += len(nums2) - second
                first += 1
            else:
                second += 1
        
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
                
    def mergeSort(self, left, right, arr, diff):
        if left == right:
            return [arr[left]]
        mid = left + (right - left) // 2
        left_half = self.mergeSort(left, mid, arr, diff)
        right_half = self.mergeSort(mid + 1, right, arr, diff)

        return self.merge(left_half, right_half, diff)

        