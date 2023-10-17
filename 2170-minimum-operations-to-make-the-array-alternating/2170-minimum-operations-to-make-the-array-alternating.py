class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        if len(set(nums)) == 1:
            return len(nums) // 2
        
        evenCnt = defaultdict(int)
        oddCnt = defaultdict(int)
        
        for i, v in enumerate(nums):
            if i % 2 == 0:
                evenCnt[v] += 1
            
            else:
                oddCnt[v] += 1
        
        totalOdd = len(nums) // 2
        
        totalEven = totalOdd
        if len(nums)%2 != 0:
            totalEven += 1
        
        heapEven = []
        for key in evenCnt:
            heappush(heapEven, -evenCnt[key])
        
        heapOdd = []
        for key in oddCnt:
            heappush(heapOdd, -oddCnt[key])
        
        max_even = -heappop(heapEven)
        max_odd = -heappop(heapOdd)
        
        max_even_key = [key for key, value in evenCnt.items() if value == max_even]
        max_odd_key = [key for key, value in oddCnt.items() if value == max_odd]
        
        if max_even_key == max_odd_key:
            if not heapEven:
                for key in max_odd_key:
                    oddCnt.pop(key)
                
                max_odd = max(oddCnt.values())
            
            elif not heapOdd:
                for key in max_even_key:
                    evenCnt.pop(key)
                
                max_even = max(evenCnt.values())
                
            elif -heapOdd[0] < -heapEven[0]:
                for key in max_even_key:
                    evenCnt.pop(key)
                
                max_even = max(evenCnt.values())
                
            else:
                for key in max_odd_key:
                    oddCnt.pop(key)
                
                max_odd = max(oddCnt.values())
        
        return totalEven - max_even + totalOdd - max_odd
    
    
    