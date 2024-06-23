class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        med_i = nums.index(k)

        left_of_med_diff_counts = collections.defaultdict(int)
        diff = 0
        for l in range(med_i - 1, -1, -1):
            diff += 1 if nums[l] < k else -1
            left_of_med_diff_counts[diff] += 1

        right_of_med_diff_counts = collections.defaultdict(int)
        diff = 0
        for r in range(med_i + 1, n):
            diff += 1 if nums[r] < k else -1
            right_of_med_diff_counts[diff] += 1

        res = left_of_med_diff_counts[0] + right_of_med_diff_counts[0] \
              + left_of_med_diff_counts[-1] + right_of_med_diff_counts[-1] + 1
        for diff, total in left_of_med_diff_counts.items():
            res += (total * right_of_med_diff_counts[-diff]) + (total * right_of_med_diff_counts[-diff - 1])
        return res