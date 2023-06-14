class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingName = kingName
        self.inheritance = defaultdict(list)
        self.dead = set()
        

    def birth(self, parentName: str, childName: str) -> None:
        self.inheritance[parentName].append(childName)
        
    def death(self, name: str) -> None:
        self.dead.add(name)
        

    def getInheritanceOrder(self) -> List[str]:
        ans = []
        
        def dfs(root):
            if not root:
                return
            
            if root not in self.dead:
                ans.append(root)
            
            for neighbour in self.inheritance[root]:
                dfs(neighbour)
        
        
        dfs(self.kingName)
        return ans


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()