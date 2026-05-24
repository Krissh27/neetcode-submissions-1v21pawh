class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph={}
        for i in range(n):
            graph[i]=[]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        h=-float('inf')
        def dfs(par,node):
            
            maxi=0
            for j in graph[node]:
                if j==par:
                    continue
                maxi=max(maxi,1+dfs(node,j))
            return maxi
        height=[0]*(n)
        for i in range(n):
            k=dfs(-1,i)
            height[i]=k
        kj=min(height)
        lis=[]
        for i in range(n):
            if height[i]==kj:
                lis.append(i)
        return lis



            
            

            
                
                
                
                

            
        