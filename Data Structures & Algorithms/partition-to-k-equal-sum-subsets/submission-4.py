class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums)%k!=0:
            return False
        target=sum(nums)//k
        numm=[False]*len(nums)
        
        def dfs(zz,s,jj):
            if zz==0:
                return True
            if s==target:
                return dfs(zz-1,0,0)
            for i in range(jj,len(nums)):
                if numm[i] or (s+nums[i])>target:
                    continue
                
                numm[i]=True
                if dfs(zz,s+nums[i],i+1):
                    return True
                numm[i]=False
            return False
        return dfs(k,0,0)




                
                


           
                
            
            


        


        

            
                



            

        
        