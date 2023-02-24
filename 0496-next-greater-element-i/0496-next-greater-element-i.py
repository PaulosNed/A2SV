class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        tracker = {}
        stack = []
        ans = [-1] * len(nums1)
        for num in nums2:
            while stack and stack[-1] < num:
                val = stack.pop()
                tracker[val] = num
            stack.append(num)
        for i,n in enumerate(nums1):
            if n in tracker:
                ans[i] = tracker[n]
        return ans