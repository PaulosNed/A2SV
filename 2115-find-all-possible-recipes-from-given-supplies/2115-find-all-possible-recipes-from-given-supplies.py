class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        graph = defaultdict(list)
        incoming = defaultdict(int)
        queue = deque()
        order = []
        sources = set(supplies)
        
        for i in range(len(recipes)):
            for ingredient in ingredients[i]:
                incoming[recipes[i]] += 1
                graph[ingredient].append(recipes[i])
        
        queue = deque(supplies)
        
        while queue:
            curr = queue.pop()
            
            if curr not in sources:
                order.append(curr)
            
            for neighbour in graph[curr]:
                incoming[neighbour] -= 1
                
                if incoming[neighbour] == 0:
                    queue.append(neighbour)
            
        
        return order
        