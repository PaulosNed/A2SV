class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        count = Counter(arr)
        
        if count[1] == 0:
            return [0, len(arr) - 1]
        
        if count[1] % 3 != 0:
            return [-1, -1]
        
        nxtOne = 1
        
        cnt = 0
        first = 0
        second = len(arr) - 2
        third = len(arr) - 2
        
        for i in range(len(arr)):
            if arr[i]:
                cnt += 1
                
                if cnt == 1:
                    first = i
                
                elif cnt == 1 + count[1] // 3:
                    second = i
                    
                elif cnt == 1 + 2 * (count[1] // 3):
                    third = i
                    
        initialFirst = first
        initialSecond = second + 1
        
        # print(first, second, third)
        while third < len(arr):
            if arr[first] == arr[second] == arr[third]:
                first += 1
                second += 1
                third += 1
            
            else:
                return [-1, -1]
        
        return [first - 1, second]