class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        check=[False]*n

        def dfs(k):
            if check[k]==True:
                return True
            check[k]=True

            for i in graph[k]:
                dfs(i)

        t=0




        for i in range(len(check)):
            if check[i]==False:
                t+=1

                dfs(i)
        return t




            



            
        