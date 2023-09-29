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
        curr.val = word
    
    def startsWith(self, prefix: str) -> None:
        curr = self.root
        for w in prefix:
            idx = ord(w) - 97
            if not curr.children[idx]:
                return []
            
            curr = curr.children[idx]
        
        def search(curr):
            if curr.is_end:
                ans.append(curr.val)
            
            if len(ans) == 3:
                return
            
            for i in range(26):
                if len(ans) < 3 and curr.children[i]:
                    search(curr.children[i])

        
        ans = []
        search(curr)
        return ans

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.val = ""
        self.children = [ None for _ in range(26) ]



class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for product in products:
            trie.insert(product)
        
        ans = []
        for i in range(1, len(searchWord) + 1):
            ans.append(trie.startsWith(searchWord[:i]))
        
        return ans