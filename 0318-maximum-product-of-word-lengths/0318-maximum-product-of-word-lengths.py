class Solution:
    def maxProduct(self, words: List[str]) -> int:
        bit_mask = [0] * len(words)
        length = [0] * len(words)
        
        for i in range(len(words)):
            for l in words[i]:
                curr = 1 << (ord(l) - ord('a'))
                bit_mask[i] = bit_mask[i] | curr
                
            length[i] = len(words[i])
        
        max_val = 0
        for i in range(len(bit_mask)):
            for j in range(i+1, len(bit_mask)):
                if bit_mask[i] & bit_mask[j] == 0:
                    max_val = max(max_val, length[i] * length[j])
                    
        return max_val