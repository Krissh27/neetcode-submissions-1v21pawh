class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pasific=set()
        atlantic= set()
        lr,lc=len(heights),len(heights[0])
        def bfs(ll,s):
            q=deque(ll)
            dr=[(1,0),(-1,0),(0,1),(0,-1)]
            for cell in ll:
                s.add(cell)

            while q:
                r,c = q.popleft()
                for nr,nc in dr:
                    if (r+nr,c+nc) not in s and 0<=r+nr<lr and 0<=c+nc<lc and heights[r][c]<=heights[r+nr][c+nc]:
                        s.add((r+nr,c+nc))
                        q.append([r+nr,c+nc])
        pacificx = []
        atlanticx = []
        for c in range(lc):
            pacificx.append((0, c))
            atlanticx.append((lr - 1, c))

        for r in range(lr):
            pacificx.append((r, 0))
            atlanticx.append((r, lc - 1))
        bfs(pacificx,pasific)
        bfs(atlanticx,atlantic)
        res = []
        for (r, c) in pasific:
            if (r, c) in atlantic:
                res.append([r, c])
        return res

                            
                        





        