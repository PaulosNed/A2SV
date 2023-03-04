class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start = 0
        end = len(arr) - 1
        while(start <= end):
            mid = start + ((end - start) // 2)
            if arr[mid] < arr[start]:
                end = mid - 1
            elif arr[mid] < arr[end]:
                start = mid + 1
            else:
                start += 1
                end -= 1
                
        return start - 1