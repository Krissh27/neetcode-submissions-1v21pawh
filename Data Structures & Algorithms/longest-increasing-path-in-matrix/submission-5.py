class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dr=[[-1, 0], [1, 0], [0, -1], [0, 1]]
        li,lj=len(matrix),len(matrix[0])
        seen=dict()
        

        def dfs(i,j,k):

            if 0<=i<li and 0<=j<lj and matrix[i][j]>k :
                if (i,j) in seen:
                    return seen[(i,j)]
                kj=0
               
                for ii,jj in dr:
                    kj=max(kj,1+dfs(i+ii,j+jj,matrix[i][j]))
                seen[(i,j)]= kj
                return seen[(i,j)]
            return 0
        maxi=0
        for i in range(li):
            for j in range(lj):
                
                maxi=max(maxi,dfs(i,j,-float('inf')))
        return maxi





        