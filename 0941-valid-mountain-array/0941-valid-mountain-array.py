class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        i = 1
        while(arr[i] > arr[i-1]):
            if i+1 >= len(arr):
                return False
            i+=1
        if i == 1:
            return False
        while(arr[i] < arr[i-1]):
            if i+1 >= len(arr):
                return True
            i += 1
        if i < len(arr):
            return False
        return True