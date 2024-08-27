class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:

        if n==1:
            return 1
        
        adjl = {}
        for road in roads:
            if road[0] not in adjl:
                adjl[road[0]] = { road[1] : road[2] }
            else:
                adjl[road[0]][road[1]] = road[2]
            if road[1] not in adjl:
                adjl[road[1]] = { road[0] : road[2] }
            else:
                adjl[road[1]][road[0]] = road[2]
        shortest  = {}
        minHeap = []
        heapq.heappush(minHeap,(0,0))
        while minHeap and len(shortest)!=n:
            k=heapq.heappop(minHeap)
            if k[1] in shortest:
                continue
            shortest[k[1]]= k[0] 
            for neighbour,weight in adjl[k[1]].items():
                if neighbour not in shortest:
                    heapq.heappush(minHeap,(weight + k[0],neighbour))
        
        heap = []
        for a,b in shortest.items():
            heapq.heappush(heap,(b*-1,a))
        
        no_of_paths = [0]*n
        no_of_paths[n-1] = 1
        while heap:
            p = heapq.heappop(heap)
            for k,_ in adjl[p[1]].items():
                if ((p[0]*-1)-adjl[p[1]][k])==shortest[k]:
                    no_of_paths[k] += no_of_paths[p[1]]
        return no_of_paths[0]%(10**9+7)