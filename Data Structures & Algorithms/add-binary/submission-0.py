class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n=max(len(a),len(b))-1
        i=len(a)-1
        j=len(b)-1
        c=0
        res=[]
        while c>0 or i>=0 or j>=0:
            if i>=0:
                da=int(a[i])
            else:
                da=0
            if j>=0:
                db=int(b[j])
            else:
                db=0
            if da+db+c<=1:
                
                res.append(da+db+c)
                c=0
            else:
                
                res.append(da+db+c-2)
                c=1
            i-=1
            j-=1
        res.reverse()
        return ''.join(map(str, res))
        
                   
        