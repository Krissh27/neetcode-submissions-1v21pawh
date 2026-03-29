class Solution:
    def decodeString(self, s: str) -> str:
        count_s=[]
        letter_s=[]
        k=0
        c=""
        for i in s:
            if i.isdigit():
                k=k*10+int(i)
            elif i == "[":
                count_s.append(k)
                letter_s.append(c)
                k=0
                c=""
            elif i  == "]":
                count=count_s.pop()
                temp=c
                c=letter_s.pop()
                c+=count*temp
                
            else:
                c+=i
        return c


                
            


        
        
         
            
           

            

                