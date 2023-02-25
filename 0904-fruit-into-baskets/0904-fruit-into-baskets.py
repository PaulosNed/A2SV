class Solution(object):
    def totalFruit(self, fruits):
        picked = {}
        start = 0
        end = 0
        max_length = 0
        while(end < len(fruits)):
            if len(picked) < 2 or fruits[end] in picked:
                picked[fruits[end]] = picked.get(fruits[end], 0) + 1
                end += 1
            else:
                max_length = max(max_length, end - start)
                picked[fruits[start]] -= 1
                if picked[fruits[start]] == 0:
                    picked.pop(fruits[start])
                start += 1
        max_length = max(max_length, end-start)
        return max_length