class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sbkp=s
        op=""
        i=0
        while i<len(t):
            if len(s)<=0 or op==sbkp:
                break
            if t[i]==s[0]:
                op+=t[i]
                s=s[1:]
            i+=1
        print(op)
        print(sbkp)
        if op==sbkp:
            return True
        else:
            return False