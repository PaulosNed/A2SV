class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        mylist=[x for x in range(1,n+1)]
        position=-1
        while len(mylist)>1:
            position = position + k
            position = position%(len(mylist))
            mylist.pop(position)
            position -= 1
        return mylist[0]