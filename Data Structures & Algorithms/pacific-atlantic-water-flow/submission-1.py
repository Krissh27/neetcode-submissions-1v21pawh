class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pasific=set()
        atlantic= set()
        lr,lc=len(heights),len(heights[0])
        dr=[(1,0),(0,1),(-1,0),(0,-1)]
        def dfs(r,c,s,h):
            if 0<=r<lr and 0<=c<lc and (r,c) not in s and heights[r][c]>=h:
                s.add((r,c))
                for nr,nc in dr:
                    dfs(r+nr,c+nc,s,heights[r][c])
        for r in range(lr):
            dfs(r,0,pasific,heights[r][0])
            dfs(r,lc-1,atlantic,heights[r][lc-1])
        for c in range(lc):
            dfs(0,c,pasific,heights[0][c])
            dfs(lr-1,c,atlantic,heights[lr-1][c])
        res=[]
        for r in range(lr):
            for c in range(lc):
                if (r,c) in atlantic and (r,c) in pasific:
                    res.append([r,c])
        return res




        



           
                        





        