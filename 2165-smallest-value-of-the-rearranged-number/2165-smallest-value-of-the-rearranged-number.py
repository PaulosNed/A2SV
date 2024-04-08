class Solution:
    def smallestNumber(self, num: int) -> int:
        
        postive = True
        if num < 0:
            postive = False
            num *= -1
            
        s = str(num)
        list_num = list(map(int, list(s)))
        
        if postive:
            list_num.sort()
        
        else:
            list_num.sort(reverse=True)
        
        i = 0
        while i < len(list_num) and list_num[i] == 0:
            i += 1
        
        if i < len(list_num):
            list_num[0], list_num[i] = list_num[i], list_num[0]
        
        str_num = "".join(list(map(str, list_num)))
        
        return int(str_num) if postive else -int(str_num)
        
        
        