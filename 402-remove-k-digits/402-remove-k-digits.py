class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stk=[]
        for i in num:
            while k and stk and stk[-1]>i:
                stk.pop()
                k-=1
            stk.append(i)
        return ''.join(stk[:-k or None]).lstrip("0") or "0"
        