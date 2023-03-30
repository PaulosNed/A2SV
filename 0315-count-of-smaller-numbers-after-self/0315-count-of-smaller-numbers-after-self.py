class Solution:
    def __init__(self):
        self.count = []
        
    def countSmaller(self, nums: List[int]) -> List[int]:
        self.count = [0] * len(nums)
        for i in range(len(nums)):
            nums[i] = [nums[i], i]
        self.mergeSort(0, len(nums)-1, nums)
        return self.count
    
    def merge(self, nums1: List[int], nums2: List[int]) -> None:
        first = 0
        second = 0
        ans = []
        cnt = 0
        while(first < len(nums1) and second < len(nums2)):
            if nums1[first] <= nums2[second]:
                ans.append(nums1[first])
                self.count[nums1[first][1]] += cnt
                first += 1
            else:
                cnt += 1
                ans.append(nums2[second])
                second += 1
                
        ans.extend(nums2[second:])
        while first < len(nums1):
            ans.append(nums1[first])
            self.count[nums1[first][1]] += cnt
            first += 1
        return ans
                
    def mergeSort(self, left, right, arr):
        if left == right:
            return [arr[left]]
        mid = left + (right - left) // 2
        left_half = self.mergeSort(left, mid, arr)
        right_half = self.mergeSort(mid + 1, right, arr)

        return self.merge(left_half, right_half)

        