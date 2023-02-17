class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        start = 0
        end = 0
        ans = 0
        while(start < len(players) and end < len(trainers)):
            if players[start] <= trainers[end]:
                ans += 1
                start += 1
            end += 1
        return ans