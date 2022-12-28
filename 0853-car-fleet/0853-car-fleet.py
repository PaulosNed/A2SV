class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        timeList = []
        complete = {}
        for i in range(len(position)):
            timeList.append((target - position[i])/speed[i])
            complete[position[i]] = timeList[i]
        position.sort()
        position.reverse()
        fleet = 1
        prev = position[0]
        for pos in position[1:]:
            if complete[pos] > complete[prev]:
                fleet += 1
                prev = pos
        return fleet
                