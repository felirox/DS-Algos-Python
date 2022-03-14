class Solution:
    def simplifyPath(self, path: str) -> str:
        stkop=[]
        for i in path.split("/"):
            if i=="..":
                if stkop:
                    stkop.pop()
            elif i and i!=".":
                stkop.append(i)
        return "/"+"/".join(stkop)
                
        