class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph={i:[] for i in range(numCourses)}
        for i in prerequisites:
            graph[i[0]].append(i[1])
        precheck={i:set() for i in range(numCourses)}
        check=[False]*numCourses

        def dfs(i):
            if check[i]==True:
                return False
            check[i]=True
            for j in graph[i]:
                if dfs(j):
                    precheck[i]|=precheck[j]
                    precheck[i].add(j)
                    
            check[i]=False
            graph[i]=[]
            
            return True
        res=[]
        for i in range(numCourses):
            dfs(i)
        for i in queries:
            if i[1] in precheck[i[0]]:
                res.append(True)
            else:
                res.append(False)
        return res





            

                    
         





                






            



        
            


        
        