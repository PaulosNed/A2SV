class Solution:
    def countVowels(self, word: str) -> int:
        cnt = 0
        vowel = {'a', 'e', 'i', 'o', 'u'}
        
        for i, letter in enumerate(word):
            if letter in vowel:
                cnt += ((i + 1) * (len(word) - i))
        
        return cnt