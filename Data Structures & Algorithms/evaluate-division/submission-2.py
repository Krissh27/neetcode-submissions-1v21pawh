class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = collections.defaultdict(list)
        for i in range(len(values)):
            a,b=equations[i]
            val=values[i]
            adj[a].append((b,val))
            adj[b].append((a,1/val))
        def dfs(srt,des,visit):
            if srt not in adj or des not in adj :
                return -1
            if srt == des:
                return 1
            visit.add(srt)
            for a,val in adj[srt]:
                if a not in visit:
                    result=dfs(a,des,visit)
                    if result!=-1:
                        return result*val
            return -1
        res=[]
        for i in queries:
            res.append(dfs(i[0],i[1],set()))
        return res









        