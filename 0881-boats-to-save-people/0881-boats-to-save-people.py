class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        start = 0
        end = len(people) - 1
        boat = 0
        while(start < end):
            weight = people[start] + people[end]
            if weight > limit:
                boat += 1
                end-=1
            else:
                boat += 1
                start += 1
                end -= 1
        if start == end:
            return boat+1
        return boat
                    