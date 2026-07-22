class Solution:
    def getSum(self, a: int, b: int) -> int:
        x=(a^b)
        an=(a&b)
        carry=0
        res=0
        for i in range(32):
            n=(x>>i)&1
            nn=(an>>i)&1
            s=carry^n
            res |= (s << i)
            carry=nn|(carry & n)
        MASK = 0xFFFFFFFF
        MAX = 0x7FFFFFFF

        res &= MASK
        return res if res <= MAX else ~(res ^ MASK)
        





            

            

            
        