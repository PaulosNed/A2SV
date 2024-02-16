class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr)
        counts = list(counter.values())
        counts.sort()
        print(counts)
        rem = len(counts)
        
        i = 0
        while i < len(counts) and k > 0:
            if counts[i] > k:
                return rem
            
            rem -= 1
            k -= counts[i]
            i += 1
        
        return rem