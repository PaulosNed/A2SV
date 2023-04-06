class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = Counter(deck)
        count_list = list(set(count.values()))
        if len(count_list) == 1:
            print(count_list)
            return count_list[0] != 1
        
        curr = self.GCD(count_list[0], count_list[1])
        for i in range(3, len(count_list)):
            curr = self.GCD(curr, count_list[i])
            
        return curr != 1
    
    def GCD(self, num1, num2):
        if not num1:
            return num2
        if not num2:
            return num1
        
        return self.GCD(num2, num1 % num2)