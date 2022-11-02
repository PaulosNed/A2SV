class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        allFlight = {}
        ans = [0] * n
        prefixSum = 0
        for booking in bookings:
            allFlight[booking[0]] = allFlight.get(booking[0], 0) + booking[2]
            allFlight[booking[1]+1] = allFlight.get(booking[1]+1, 0) - booking[2]
        for i in range(1, n+1):
            if i in allFlight:
                prefixSum += allFlight[i]
            ans[i-1] = prefixSum
        return ans