class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        
        i = len(arr) - 1
        while i >= 0:
            j = i + 1
            flag = False
            curr_idx = None
            while j < len(arr):
                if arr[i] > arr[j]:
                    flag = True
                    if not curr_idx or arr[j] > arr[curr_idx]:
                        curr_idx = j
                j += 1
            
            if flag:
                arr[i], arr[curr_idx] = arr[curr_idx], arr[i]
                return arr

            i -= 1
        
        return arr