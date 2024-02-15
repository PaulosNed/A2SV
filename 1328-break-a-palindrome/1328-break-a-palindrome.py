class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        start = 0
        end = len(palindrome) - 1
        palindrome = list(palindrome)
        
        
        while start < end:
            if palindrome[start] != "a":
                palindrome[start] = "a"
                return "".join(palindrome)
            
            start += 1
            end -= 1
        
        if len(palindrome) > 1 and len(set(palindrome)) == 1:
            palindrome[-1] = "b"
            return "".join(palindrome)
        
        elif len(palindrome) != 1 and start == end:
            palindrome[-1] = "b"
            return "".join(palindrome)
        
        
        return ""