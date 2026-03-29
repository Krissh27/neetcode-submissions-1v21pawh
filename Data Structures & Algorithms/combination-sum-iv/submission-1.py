class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        num=[-1]*(target+1)
        def dfs(i):
            if i ==target:
                return 1
            
            if num[i]!=-1:
                return num[i] 
            kk=0
            for j in nums:
                if j+i>target:
                    continue
                kk=dfs(j+i)+kk
            num[i]=kk
            
            return kk
        return dfs(0)
        
