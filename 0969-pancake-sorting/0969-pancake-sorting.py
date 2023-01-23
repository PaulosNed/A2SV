class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        next = len(arr)+1
        i = 0
        j = arr.index(next-1)+1
        ans = []
        while(next != 1):
            next -= 1
            i = 0
            j = arr.index(next)
            if (j+1 == next):
                continue
            ans.append(j+1)
            while(i<j):
                arr[i], arr[j] = arr[j], arr[i]
                i+=1
                j-=1
            i=0
            j = arr[0] - 1
            ans.append(j+1)
            while(i<j):
                arr[i], arr[j] = arr[j], arr[i]
                i+=1
                j-=1 
        return ans