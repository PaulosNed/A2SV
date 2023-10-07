class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nums = int(''.join(map(str, digits)))

        nums += 1
        
        nums = str(nums)
        
        final_list = [int(num) for num in nums]
        
        return final_list
        