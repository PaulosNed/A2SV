class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        idx = 0
        opened = False
        i = 0
        while idx < len(source):
            val = source[idx]
            while(i < len(val)):
                if val[i] == "/":
                    if not opened and i+1 < len(val):
                        if val[i+1] == "*":
                            opened = True
                            val = val[:i] + val[i+2:]
                        elif val[i+1] == "/":
                            # print(val, i)
                            val = val[:i]
                            break
                if val[i] == "*":
                    if i+1 < len(val) and val[i+1] == "/" and opened:
                        opened = False
                        val = val[:i] + val[i+2:]
                if opened:
                    val = val[:i] + val[i+1:]
                else:
                    if i <len(val) and val[i] == "/" and i+1 < len(val) and (val[i+1] == "*" or val[i+1] =="/"):
                        continue
                    i+=1
            if val == "":
                source.pop(idx)
                i=0
            else:
                source[idx] = val
                if opened and idx + 1 < len(source):
                    source[idx] += source[idx+1]
                    source.pop(idx+1)
                    i = len(val)
                else:
                    idx += 1
                    i = 0
        return source
            