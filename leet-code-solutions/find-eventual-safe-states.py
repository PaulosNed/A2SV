class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        colors = [0 for _ in range(len(graph))]
        order = []
        
        for node in range(len(graph)):
            if colors[node] != 0:
                continue
            
            self.topSort(node, colors, graph, order)
            
        order.sort()
        return order
    
    def topSort(self, node, colors, graph, order):
        if colors[node] == 1:
            return False
        
        colors[node] = 1
        
        for neighbour in graph[node]:
            if colors[neighbour] == 2:
                continue
            
            if not self.topSort(neighbour, colors, graph, order):
                return False
        
        order.append(node)
        colors[node] = 2
        return True
        
        
                