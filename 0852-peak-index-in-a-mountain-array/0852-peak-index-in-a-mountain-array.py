class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        idx = 0
        for i in range(len(arr)):
            if arr[i] > arr[idx]:
                idx = i
        return idx