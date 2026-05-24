class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        visit=[False]*(n+1)
        graph={}
        for i in range(n+1):
            graph[i]=[]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        cycleS=-1
        cycle=set()
        def dfs(par,node):
            nonlocal cycleS
            if visit[node]==True:
                cycleS=node
                return True
            visit[node]=True
            for j in graph[node]:
                if j==par:
                    continue
                if dfs(node,j):
                    if cycleS!=-1:
                        cycle.add(j)
                    if cycleS==node:
                        cycleS=-1
                    return True
            return False
        dfs(-1,1)
        for u,v in reversed(edges):
            if u in cycle and v in cycle:
                return [u,v]
        return []
                
                    



        