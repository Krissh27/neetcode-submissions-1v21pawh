class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        rank = [0] * n
        parent = [i for i in range(n)]

        def find(y):
            x = y
            while x != parent[x]:
                x = parent[x]
            parent[y] = x  # path compression
            return x

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False  # already connected -> redundant edge
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1
            return True

        for s, e in edges:
            if not union(s - 1, e - 1):
                return [s, e]

        return []