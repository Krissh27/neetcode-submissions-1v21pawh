class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1:
            return False
        parent=[0]*n
        for i in range(n):
            parent[i]=i
        rank=[0]*n
        def find(y):
            x=y
            while parent[x]!=x:
                x=parent[x]
            parent[y]=x
            return x
    
        def union(x,y):
            px,py=find(x),find(y)
            if px==py:
                return False
            if rank[py]>rank[px]:
                px,py=py,px
            parent[py]=px
            if rank[py]==rank[px]:
                rank[px]+=1
            return True
        for s,e in edges:
            if not union(s,e):
                return False
        return True







