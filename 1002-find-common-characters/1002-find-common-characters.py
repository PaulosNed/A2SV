class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        word_pos = []
        
        for word in words:
            alphabets = [0 for alph in range(26)]
            for letter in word:
                alphabets[ord(letter) - 97] += 1
            word_pos.append(alphabets)
        # print(alphabets)
        output = []
        for idx in range(26):
            count = float("inf")
            for alphabet in word_pos:
                count = min(count, alphabet[idx])
            for i in range(count):
                output.append(chr(idx + 97))
        return output