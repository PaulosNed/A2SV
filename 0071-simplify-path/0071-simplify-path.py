class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        final = []
        for p in path:
            if p == ".." and final:
                final.pop()
            elif p == "." or p == "" or p == "..":
                continue
            else:
                final.append("/" + p)
        if not final:
            return "/"
        return "".join(final)