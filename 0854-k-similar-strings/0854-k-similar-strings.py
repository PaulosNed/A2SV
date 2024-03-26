class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        def get_neighbors(s, s2):
            i = 0
            while s[i] == s2[i]: i += 1 # find char that is different to swap
            for j in range(i+1, len(s)):
                if s[j] == s2[i] and s[j] != s2[j]: # only swap if getting closer to s2
                    # swap s[i] with s[j]
                    yield s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]

        if s1 == s2: return 0

        queue = deque([(s1, 0)])
        visited = set()

        while queue:
            s, k = queue.popleft()
            if s == s2: return k
            for n in get_neighbors(s, s2):
                if n in visited: continue
                visited.add(n)
                queue.append((n, k+1))
        return -1