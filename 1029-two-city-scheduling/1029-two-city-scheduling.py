class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        cityA = []
        cityB = []
        diff = []
        
        for i in range(len(costs)):
            diff.append([abs(costs[i][0] - costs[i][1]) , i])
        
        diff.sort(reverse=True)
        
        for i in range(len(diff)):
            idx = diff[i][1]
            currA, currB = costs[idx][0], costs[idx][1]
            
            if currA <= currB and len(cityA) < len(costs) // 2:
                cityA.append(currA)
            
            else:
                if len(cityB) < len(costs) // 2:
                    cityB.append(currB)
                else:
                    cityA.append(currA)
        
        return sum(cityA) + sum(cityB)