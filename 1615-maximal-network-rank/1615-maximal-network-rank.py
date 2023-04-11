class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for road in roads:
            graph[road[0]].append((min(road[1], road[0]), max(road[0], road[1])))
            graph[road[1]].append((min(road[1], road[0]), max(road[0], road[1])))
        
        max_roads = 0
        for node1 in graph:
            for node2 in graph:
                curr = len(set(graph[node1] + graph[node2]))
                max_roads = max(curr, max_roads)
        
        return max_roads