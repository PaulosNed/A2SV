class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = []
        while(columnNumber > 26):
            ordx = columnNumber%26
            if ordx == 0:
                ordx = 26
                columnNumber = (columnNumber//26) - 1
            else:
                columnNumber = columnNumber//26
            ans.append(chr(ordx + 64))
        ans.append(chr(columnNumber+64))
        ans.reverse()
        return "".join(ans)