class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        check=[False]*n
        checkk=True

        def dfs(n,p):
            nonlocal checkk
            
            if check[n]==True:
                return False
            check[n]=True
            for i in graph[n]:
                if i==p:
                    continue
                if not dfs(i,n):
                    return False

            return True
        kk=True
        rizz=dfs(0,-1)
        for i in check:
            if i ==False:
                kk=False
        

        
        return kk and rizz






        