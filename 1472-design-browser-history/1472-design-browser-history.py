class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.visited= [homepage]
        self.backward = []

    def visit(self, url: str) -> None:
        self.visited.append(url)
        self.backward.clear()
    def back(self, steps: int) -> str:
        while len(self.visited)>1 and steps:
            steps-=1
            self.backward.append(self.visited.pop())
        return self.visited[-1]
    def forward(self, steps: int) -> str:
        while self.backward and steps:
            steps-=1
            self.visited.append(self.backward.pop())
        return self.visited[-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)