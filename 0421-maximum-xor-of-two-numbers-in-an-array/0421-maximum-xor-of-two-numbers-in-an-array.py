class Solution(object):
    def findMaximumXOR(self, nums):
        
        trie = {}
        def update_trie(x):
            cur = trie
            for bit in format(x, '032b'):
                
                if bit not in cur:
                    cur[bit] = {}
                cur = cur[bit]
                
            cur['value'] = x
            
            return
             
        def best_match(x):
            cur = trie
            for bit in format(x, '032b'):
                
                rev = '0' if bit == '1' else '1'
                if rev in cur:
                    cur = cur[rev]
                else:
                    cur = cur[bit]
                    
            return cur['value']
        
        for x in nums:
            update_trie(x)
        
        max_xor = 0
        for x in nums:
            max_xor = max( max_xor, x ^ best_match(x) )
         
        return max_xor