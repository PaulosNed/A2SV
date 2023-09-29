class Trie:
    def __init__(self):
        self.root = TrieNode(True)
        self.longest = ""
    
    def insert(self, key: str) -> None:
        curr = self.root
        parent = None
            
        for w in key:
            idx = ord(w) - 97
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            
            parent = curr
            curr = curr.children[idx]
        
        if parent.is_valid:
            if len(key) > len(self.longest):
                self.longest = key
            
            curr.is_valid = True
    
    
class TrieNode:
    def __init__(self, is_valid = False):
        self.is_valid = is_valid
        self.children = [ None for _ in range(26) ]


class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        trie = Trie()
        
        for word in words:
            trie.insert(word)
        
        return trie.longest