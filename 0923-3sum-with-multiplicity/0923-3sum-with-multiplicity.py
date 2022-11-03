class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        arr.sort()
        reps = Counter(arr)
        i = 0
        end = len(arr)-1
        ans = 0
        while(i < len(arr)):
            j = i
            k = end
            while(j < k):
                if arr[i]+arr[j]+arr[k] < target:
                    j += reps[arr[j]]
                elif arr[i]+arr[j]+arr[k] > target:
                    k -= reps[arr[k]]
                else:
                    if arr[i] != arr[j] != arr[k]:
                        ans += (reps[arr[i]]*reps[arr[j]]*reps[arr[k]])
                    elif arr[i] == arr[j] == arr[k]:
                        ans += math.comb(reps[arr[i]], 3)
                    elif arr[i] == arr[j]:
                        ans += (math.comb(reps[arr[i]], 2)*reps[arr[k]])
                    else:
                        ans += (reps[arr[i]]*math.comb(reps[arr[j]], 2))
                    j += reps[arr[j]]
                    k -= reps[arr[k]]
            i += reps[arr[i]]
        return ans % 1000000007