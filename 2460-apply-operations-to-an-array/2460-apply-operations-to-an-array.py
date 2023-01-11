class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        start = 1
        write = []
        read = 0
        while(start < len(nums)):
            if nums[start-1] == nums[start]:
                nums[start-1] = nums[start-1] * 2
                nums[start] = 0
            start += 1
        while(read < len(nums)):
            if nums[read] == 0:
                write.append(read)
            elif nums[read] != 0 and write:
                nums[write[0]], nums[read] = nums[read],nums[write[0]]
                write.pop(0)
                write.append(read)
            read += 1
        return nums