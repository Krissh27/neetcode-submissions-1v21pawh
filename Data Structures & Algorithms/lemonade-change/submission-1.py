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
            if change==5:
                if mapi[5]>0:
                    mapi[5]-=1
                    continue
                else:
                    return False
            if change==15:
                if mapi[10]>0 and mapi[5]>0:
                    mapi[5]-=1
                    mapi[10]-=1
                    continue
                elif mapi[5]>2:
                    mapi[5]-=3
                    continue
                else:
                    return False

                

        return True



                
        