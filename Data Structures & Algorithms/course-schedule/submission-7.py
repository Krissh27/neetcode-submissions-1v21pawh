class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph={i:[] for i in range(numCourses)}
        for i in prerequisites:
            graph[i[0]].append(i[1])
        check=[False]*numCourses

        def dfs(i):
            if check[i]==True:
                return False
            check[i]=True
            for j in graph[i]:
                if not dfs(j):
                    return False
            check[i]=False
            graph[i]=[]
            return True
        
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
        
        
            



                
            







        