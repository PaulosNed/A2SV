class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if len(s) == 1:
            return [1]
        firstApp = {}
        lastApp = {}
        allApps = []
        final = []
        for idx,letter in enumerate(s):
            if letter not in firstApp:
                firstApp[letter] = idx
        pointer = len(s) - 1
        while(pointer >= 0):
            if s[pointer] not in lastApp:
                lastApp[s[pointer]] = pointer
            pointer -= 1
        for key in firstApp:
            allApps.append([firstApp[key], lastApp[key]])
        allApps.sort(key = lambda x:x[0])
        start = 0
        end = 1
        while(end < len(allApps)):
            if allApps[end][0] > allApps[start][1]:
                final.append(allApps[start][1] - allApps[start][0] + 1)
                start = end
            else:
                allApps[start][1] = max(allApps[start][1], allApps[end][1])
            end += 1
        final.append(allApps[start][1] - allApps[start][0] + 1)
        return final