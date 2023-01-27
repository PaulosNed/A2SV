class Node:
    def __init__(self, val = 0, nextNode = None):
        self.val = val
        self.next = nextNode
        
class MyLinkedList:
    def __init__(self):
        self.dummy = Node()

    def get(self, index: int) -> int:
        curr = self.dummy.next
        idx = 0
        for _ in range(index):
            if curr == None:
                return -1
            curr = curr.next
            idx += 1
        if curr == None:
            return -1
        return curr.val
    
    def getReturn(self, index: int) -> int:
        curr = self.dummy.next
        for _ in range(index):
            if curr == None:
                return None
            curr = curr.next
        return curr
    
    def addAtHead(self, val: int) -> None:
        curr = Node(val)
        curr.next = self.dummy.next
        self.dummy.next = curr

    def addAtTail(self, val: int) -> None:
        currNode = Node(val)
        tail = self.dummy
        while(tail.next):
            tail = tail.next
        tail.next = currNode

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            prev = self.dummy
        else:
            prev = self.getReturn(index-1)
        if prev:
            curr = Node(val)
            curr.next = prev.next
            prev.next = curr

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            prev = self.dummy
        else:
            prev = self.getReturn(index-1)
        if prev and prev.next:
            prev.next = prev.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)