class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        size = 0
        noOfItems = 0
        for i in nums:
            if i in count.keys():
                count[i]+=1
            else:
                count[i] = 1
        sortedDict = dict(sorted(count.items(), key=lambda item: item[1]))
        sortedKeys = list(sortedDict.keys())
        sortedKeys.reverse()
        return sortedKeys[:k]