class Solution(object):
    def totalFruit(self, fruits):
        if len(fruits) <= 2:
            return len(fruits)
        largest = 0
        first = 0
        second = 1
        bucket = {fruits[first]}
        while (second < len(fruits)):
            if len(bucket) > 2:
                first += 1
                second += 1
                bucket = set(fruits[first:second])
            elif fruits[second] in bucket:
                second+=1
            elif len(bucket) < 2:
                bucket.add(fruits[second])
                second+=1
            else:
                largest = max(largest, second-first)
                first += 1
                second += 1
                bucket = set(fruits[first:second])
        largest = max(largest, second-first)
        return largest