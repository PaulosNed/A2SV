class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = 0
        while(i< len(s)):
            if s[i] == "#":
                # print(chr(int(s[i-2:i]) + 96))
                print(s)
                s = s[:i-2] + chr(int(s[i-2:i]) + 96) + s[i+1:]
                i-=2
            else:
                i+=1
        for i in range(len(s)):
            if s[i].isdigit():
                temp = chr(int(s[i])+96)
                s = s[:i] + temp + s[i+1:]
        return s