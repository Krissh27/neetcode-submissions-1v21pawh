class Solution:
    def isHappy(self, n: int) -> bool:
        k=set()
        num=n
        while True:
            if num in k:
                return False
            
            elif num ==1:
                break
            
            k.add(num)
            temp=0
            while num:
                temp+=(num%10)**2
                num=num//10
            num=temp
        return True
            
            

        