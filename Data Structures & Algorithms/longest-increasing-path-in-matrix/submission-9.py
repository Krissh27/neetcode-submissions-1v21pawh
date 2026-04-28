import sys
sys.setrecursionlimit(200*200 + 1000)
class Solution:

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp={}
        r=len(matrix)
        c=len(matrix[0])
        direc=[(0,1),(0,-1),(1,0),(-1,0)]
        def dfs(rr,cc):
            
                
            if (rr,cc) in dp:
                return dp[(rr,cc)]
            res=1
            for i,j in direc:
                nr=rr+i
                nc=cc+j
                if 0<=nr<r and 0<=nc<c and matrix[nr][nc]>matrix[rr][cc]:
                    res=max(res,1+dfs(rr+i,cc+j))
            dp[(rr,cc)]=res
            return dp[(rr,cc)]
        maxi=0
        for i in range(r):
            for j in range(c):
                maxi=max(maxi,dfs(i,j))
        return maxi




            




        