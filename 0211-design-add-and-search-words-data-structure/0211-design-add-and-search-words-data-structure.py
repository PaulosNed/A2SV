class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        
        for w in word:
            idx = ord(w) - 97
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            
            curr = curr.children[idx]
        
        curr.is_end = True
        

    def search(self, word: str) -> bool:
        curr = self.root
        
        for i in range(len(word)):
            if word[i] == '.':
                for j in range(26):
                    newWord = word[:i] + chr(97+j) + word[i+1:]
                    if self.search(newWord):
                        return True
                
                return False
            
            else:
                idx = ord(word[i]) - 97
                if not curr.children[idx]:
                    return False

                curr = curr.children[idx]
        
        return curr.is_end
        
        
class TrieNode:
    
    def __init__(self):
        self.is_end = False
        self.children = [None for i in range(26)]

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)