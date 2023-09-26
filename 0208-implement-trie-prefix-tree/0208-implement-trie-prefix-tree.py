class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        curr = self.root
        for w in word:
            idx = ord(w) - 97
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            
            curr = curr.children[idx]
        
        curr.is_end = True
    
    def startsWith(self, prefix: str) -> None:
        curr = self.root
        for w in prefix:
            idx = ord(w) - 97
            if not curr.children[idx]:
                return False
            
            curr = curr.children[idx]
        
        return True
    
    def search(self, word: str) -> None:
        curr = self.root
        for w in word:
            idx = ord(w) - 97
            if not curr.children[idx]:
                return False
            
            curr = curr.children[idx]
        
        return curr.is_end

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]




# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)