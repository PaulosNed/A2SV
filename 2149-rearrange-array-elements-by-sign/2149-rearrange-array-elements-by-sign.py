class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives = []
        negatives = []
        ans = []
        for idx, num in enumerate(nums):
            if num < 0:
                negatives.append(num)
            else:
                positives.append(num)
        for i in range(len(positives)):
            ans.extend([positives[i], negatives[i]])
        return ans
        