class MapSum:

    def __init__(self):
        self.root = [TrieNode(), 0]
        self.existing = {}
        
    def insert(self, key: str, val: int) -> None:
        curr = self.root
        initial = val
        
        if key in self.existing:
            val -= self.existing[key]
        
        self.existing[key] = initial
            
        for w in key:
            idx = ord(w) - 97
            if not curr[0].children[idx]:
                curr[0].children[idx] = [TrieNode(), 0]
            
            curr[0].children[idx][1] += val
            curr = curr[0].children[idx]
        
        curr[0].is_end = True
    
    def search(self, word: str) -> None:
        curr = self.root
        
        for w in word:
            idx = ord(w) - 97
            if not curr[0].children[idx]:
                return 0
            
            curr = curr[0].children[idx]
        
        return curr[1]

    def sum(self, prefix: str) -> int:
        return self.search(prefix)

        
class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]



# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)