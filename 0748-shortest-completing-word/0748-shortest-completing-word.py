class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        hidden = []
        def hidden_alphabets():
            for i in range(len(licensePlate)):
                if not licensePlate[i].isdigit():
                    if licensePlate[i] != " ":  
                        hidden.append(licensePlate[i].lower())
        hidden_alphabets()
        index = -1
        minimum = float("inf")
        flag = False
        for i,word in enumerate(words):
            flag = False
            for one_hidden_alphabet in hidden:
                if one_hidden_alphabet in word:
                    word = word.replace(one_hidden_alphabet,'', 1)
                else:
                    flag = True
                    break
            if minimum > len(word) and not flag:
                minimum = len(word)
                index = i 
        return words[index]