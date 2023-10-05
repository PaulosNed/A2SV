class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        
        evenNums = []
        
        for num in nums:
            
            if num % 2 == 0:
                evenNums.append(num)
        
        if not evenNums:
            return -1
        
        count = Counter(evenNums)
        max_val = max(count.values())
        
        evenNums.sort()
        
        for num in evenNums:
            if count[num] == max_val:
                return num