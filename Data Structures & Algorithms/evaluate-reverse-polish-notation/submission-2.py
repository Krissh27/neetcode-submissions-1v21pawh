class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        self.list1=[]
        for i in range(len(tokens)):
            k=0
            if tokens[i] in "+-/*":
                j=self.list1.pop()
                m=self.list1.pop()
                if tokens[i]=="+":
                     k=m+j
                if tokens[i]=="*":
                    k=m*j
                if tokens[i]=="/":
                    k=m/j
                if tokens[i]=="-":
                    k=m-j
                self.list1.append(int(k))
            else:
                self.list1.append(int(tokens[i]))

        return self.list1[-1]













        '''for i in range(3):
            if tokens[i]=="+":
                k=int(tokens[i-2])+int(tokens[i-1])
            if tokens[i]=="*":
                k=int(tokens[i-2])*int(tokens[i-1])
            if tokens[i]=="/":
                k=int(tokens[i-2])/int(tokens[i-1])
            if tokens[i]=="-":
                k=int(tokens[i-2])-int(tokens[i-1])

        for i in range(3,len(tokens)):
            if tokens[i]=="+":
                k=k+int(tokens[i-1])
            if tokens[i]=="*":
                k=k*int(tokens[i-1])
            if tokens[i]=="/":
                k=k/int(tokens[i-1])
            if tokens[i]=="-":
                k=k-int(tokens[i-1])
        return k

            

            
        '''