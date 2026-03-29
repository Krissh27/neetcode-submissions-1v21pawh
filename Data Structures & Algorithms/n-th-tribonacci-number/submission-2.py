class Solution:
    def tribonacci(self, n: int) -> int:
        lil=[0,1,1]
        if n<3:
            return lil[n]
        kk=[-1]*(n+1)
        kk[0]=0
        kk[1]=1
        kk[2]=1
        
        for i in range(3,n+1):
            zz=0
            for j in range(1,4):
                zz+=kk[i-j]
                kk[i]=zz
        return kk[n]
                    