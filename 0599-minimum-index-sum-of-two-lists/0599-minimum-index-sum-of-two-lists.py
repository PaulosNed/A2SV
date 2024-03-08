class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        tracker1 = {}
        tracker2 = {}
        
        for idx, val in enumerate(list1):
            tracker1[val] = idx
        
        for idx, val in enumerate(list2):
            tracker2[val] = idx
        
        min_var = float("inf")
        ans = []
        for key in tracker1:
            if key in tracker2:
                if tracker1[key] + tracker2[key] < min_var:
                    ans = [key]
                    min_var = tracker1[key] + tracker2[key]
                elif tracker1[key] + tracker2[key] == min_var:
                    ans.append(key)
        
        return ans
            