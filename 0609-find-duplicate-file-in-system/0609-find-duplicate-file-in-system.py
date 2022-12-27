class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        tracker = defaultdict(list)
        final = []
        for path in paths:
            path = path.split(" ")
            if len(path) <= 1:
                continue
            i = 1
            while(i < len(path)):
                path[i] = path[i].split("(")
                tracker[path[i][1]].append(path[0]+"/"+path[i][0])
                i += 1
        for value in tracker.values():
            if len(value) > 1:
                final.append(value)
        return final
                