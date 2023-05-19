class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                curr_sum = nums1[i] + nums2[j]
                if len(heap) == k:
                    if -heap[0][0] > curr_sum:
                        heappop(heap)
                    else:
                        break
                
                heappush(heap, [-curr_sum, nums1[i], nums2[j]])
        
        
        final = []
        while heap:
            val, x, y = heappop(heap)
            final.append([x, y])
        final.reverse()
        return final