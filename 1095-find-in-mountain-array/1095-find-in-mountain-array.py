# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        
        def findPeak():
            left = 0
            right = mountain_arr.length() - 1
            length = mountain_arr.length()
            
            
            while left <= right:
                mid = left + (right - left) // 2
                # print(left, right, mid)
                curr = mountain_arr.get(mid)
                left_val = mountain_arr.get(mid - 1) if mid - 1 >= 0 else -inf 
                right_val = mountain_arr.get(mid + 1) if mid + 1 < length else -inf
                
                if curr > left_val and curr > right_val:
                    return mid
                
                elif curr > left_val and right_val > curr:
                    left = mid + 1
                
                elif curr < left_val and right_val < curr:
                    right = mid - 1
        
        def findTarget(start, end):
            nonlocal target
            
            left = start
            right = end
            
            while left <= right:
                
                mid = left + (right - left) // 2
                curr = mountain_arr.get(mid)
                
                if curr > target:
                    right =  mid - 1
                
                elif curr < target:
                    left = mid + 1
                
                else:
                    return mid
            
            return -1
        
        
        def findTargetReversed(start, end):
            nonlocal target
            
            left = start
            right = end
            
            while left <= right:
                
                mid = left + (right - left) // 2
                curr = mountain_arr.get(mid)
                
                if curr < target:
                    right =  mid - 1
                
                elif curr > target:
                    left = mid + 1
                
                else:
                    return mid
            
            return -1
        
        mid_idx = findPeak()
        
        ans = findTarget(0, mid_idx)
        if ans == -1:
            ans = findTargetReversed(mid_idx, mountain_arr.length() - 1)
            
        return ans
                
                
                
                