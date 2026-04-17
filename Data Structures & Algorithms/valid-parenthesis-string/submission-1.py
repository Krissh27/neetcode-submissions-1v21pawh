class Solution:
    def checkValidString(self, s: str) -> bool:
        stack=[]
        star=[]
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            elif stack and s[i]==')':
                stack.pop()
            elif s[i]=="*":
                star.append(i)
            elif s[i]==')' and star:
                star.pop()
                continue
            else:
                return False


        while star and stack:
            if star.pop()<stack.pop():
                return False
        if stack:
            return False

        
        return True



        