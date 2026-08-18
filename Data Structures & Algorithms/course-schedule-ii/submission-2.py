class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        state=[0]*numCourses
        memo={i:[] for i in range(numCourses)}
        for i in prerequisites:
            memo[i[0]].append(i[1])
        order=[]


        def dfs(i):
            if state[i] == 1:
                return False       

            if state[i] == 2:
                return True        

            state[i] = 1

            for j in memo[i]:
                if not dfs(j):
                    return False
            order.append(i)

            state[i] = 2
            return True
        for i in range(numCourses):
            if state[i]==0:
                if not dfs(i):
                    return []
        return order


