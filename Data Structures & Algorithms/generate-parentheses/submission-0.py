class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        list1=[]
        stack=[]
        def count_parenthesis(o,c):
            
            if o==c==n:
                list1.append("".join(stack))
                return
            if o<n:
                stack.append("(")
                count_parenthesis(o+1,c)
                stack.pop()
            if c<n and c<o:
                stack.append(")")
                count_parenthesis(o,c+1)
                stack.pop()
            return
        count_parenthesis(0,0)
        return list1
        


        