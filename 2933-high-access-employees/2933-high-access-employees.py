class Solution:
    def time(self, t):
        return int(t[:2], 10) * 60 + int(t[2:], 10)
  
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        data, res = defaultdict(deque), set()
        for name, t in sorted(access_times, key=lambda x: x[1]):
            data[name].append(self.time(t))
            while data[name][-1] - data[name][0]>= 60:
                data[name].popleft()
            if len(data[name]) >= 3:
                res.add(name)
      
        return list(res)