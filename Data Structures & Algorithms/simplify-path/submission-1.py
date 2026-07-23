class Solution:
    def simplifyPath(self, path: str) -> str:
        res=""
        resl=[]
        i=1

        while i <len(path):
            if path[i]=="/":
                while i<len(path) and path[i]=="/":
                    i+=1
                if res==".." and resl:
                    resl.pop()
                    res=""
                elif res=='.':
                    res=""
                    pass

                else:
                    if res and res!="..":
                        resl.append(res)
                    res=''
            if i==len(path):
                break
            res+=path[i]
            i+=1
        






        if res == "..":

            if resl:

                resl.pop()

        elif res != "." and res != "":

            resl.append(res)

        return "/" + "/".join(resl)
        

                    

            