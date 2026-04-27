class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n=len(hand)
        if n%groupSize!=0:
            return False
        dic=Counter(hand)
        for i in hand:
            s=i
            if s not in dic:
                continue
            while s-1 in dic:
                s-=1
            for ii in range(s,s+groupSize):
                if ii not in dic :
                    return False
                dic[ii]-=1
                if dic[ii]==0:
                    del dic[ii]
        return True
                

            