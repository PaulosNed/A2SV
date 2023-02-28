class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        prevList = self.getRow(rowIndex-1)
        
        new = [1]
        for i in range(len(prevList)-1):
            new.append(prevList[i]+prevList[i+1])
        new.append(1)
        
        return new
        """
        RI = 0:
            [1]
        prevList = self.getRow(rowIndex-1)
        new = [1]
        for index of prevList:
            new.append(prevList[i]+prevList[i+1])
        new.append(1)
        return new
        """