class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        
        queryIPV4 = queryIP.split(".")
        
        if len(queryIPV4) == 4:
            
            for num in queryIPV4:
                try:
                    intNum = int(num)
                    if not (0 <= intNum <= 255) or (len(num) > 1 and num[0] == '0'):
                        return "Neither"
                
                except:
                    return "Neither"

            return "IPv4"
        
        queryIPV6 = queryIP.split(":")
        valid = {'a', 'b', 'c', 'd', 'e', 'f', 'A', 'B', 'C', 'D', 'E', 'F', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
        
        if len(queryIPV6) == 8:
            
            for num in queryIPV6:
                if not (1 <= len(num) <= 4):
                    return "Neither"
                
                for char in num:
                    if char not in valid:
                        return "Neither"
                
            return "IPv6"
            
        
        return "Neither"
            