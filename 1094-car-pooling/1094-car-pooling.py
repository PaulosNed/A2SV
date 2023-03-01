class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        stops = []
        occupied = 0
        for trip in trips:
            stops.append((trip[1], trip[0]))
            stops.append((trip[2], -trip[0]))
        stops.sort()
        for stop in stops:
            occupied += stop[1]
            if occupied > capacity:
                return False
        return True