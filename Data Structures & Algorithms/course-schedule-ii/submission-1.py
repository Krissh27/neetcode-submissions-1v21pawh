class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph={i:[] for i in range((numCourses)) }
        for i in prerequisites:
            graph[i[0]].append(i[1])
        check=[False]*(numCourses)
        res=[]
        def dfs(i):
            if check[i]==True:
                return False
            check[i]=True
            for j in graph[i]:
                if not dfs(j):
                    return False
            
            check[i]=False
            if i not in res:
                res.append(i)
            graph[i]=[]
            return True
        for i in range((numCourses)):
            if not dfs(i):
                return []
        return res


        




            

        