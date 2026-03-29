class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        maxi=0
        mapi={5:0,10:0,20:0}
        for i in bills:
            if i==5:
                mapi[i]+=1
                continue
            mapi[i]+=1
            change=i-5
            while change>0:
                if change>=10 and mapi[10]>0:
                    mapi[10]-=1
                    change-=10
                else:
                    if mapi[5]>0:
                        mapi[5]-=1
                        change-=5
                    else:
                        return False
        return True



                
        