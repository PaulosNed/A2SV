class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        count = defaultdict(int)
        for edge in edges:
            count[edge[0]] += 1
            count[edge[1]] += 1
        return max(count, key=count.get)