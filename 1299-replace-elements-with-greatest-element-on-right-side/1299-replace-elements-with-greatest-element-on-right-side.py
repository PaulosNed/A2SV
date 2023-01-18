class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        end = len(arr) - 1
        greatest = arr[end]
        arr[end] = -1
        end -= 1
        while(end >= 0):
            currVal = arr[end]
            arr[end] = greatest
            greatest = max(greatest, currVal)
            end -= 1
        return arr