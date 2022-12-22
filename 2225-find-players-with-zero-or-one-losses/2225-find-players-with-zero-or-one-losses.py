class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = []
        lossers = []
        zeroLoss = []
        oneLoss = []
        for match in matches:
            winners.append(match[0])
            lossers.append(match[1])
        allTeams = set(winners+lossers)
        winners = Counter(winners)
        lossers = Counter(lossers)
        for team in allTeams:
            if team not in lossers:
                zeroLoss.append(team)
        for losser in lossers:
            if lossers[losser] == 1:
                oneLoss.append(losser)
        zeroLoss.sort()
        oneLoss.sort()
        return [zeroLoss, oneLoss]
        