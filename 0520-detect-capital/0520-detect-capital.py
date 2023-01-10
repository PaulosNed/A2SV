class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        allCapitals = False
        if len(word)>=2 and "A"<=word[0]<="Z" and "A"<=word[1]<="Z":
            allCapitals = True
        for letter in word[1:]:
            if allCapitals:
                if letter < "A" or letter > "Z":
                    return False
            else:
                if letter < "a" or letter > "z":
                    return False
        return True
                