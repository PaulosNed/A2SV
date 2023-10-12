# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nestedList = nestedList
        self.ans = []
        
        for nes in self.nestedList:
            self.ans.extend(self.findValue(nes))
            
        # print(self.ans)
        self.findValue(self.nestedList)
        self.idx = 0
        
    def next(self) -> int:
        val = self.ans[self.idx]
        self.idx += 1
        
        return val
    
    def hasNext(self) -> bool:
        return self.idx < len(self.ans)
    
    def findValue(self, curr: NestedInteger):
        # print(curr, self.ans)
        if type(curr) == list:
            return
        
        if curr.isInteger():
            return [curr.getInteger()]
        
        ans = []
        options = curr.getList()
        # print("options", options)
        for item in options:
            ans.extend(self.findValue(item))
        
        return ans
        
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())