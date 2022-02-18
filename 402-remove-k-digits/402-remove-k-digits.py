class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        cos=[]
        for i in range(len(num)):
            while k and cos and cos[-1]>num[i]:
                cos.pop()
                k-=1
            cos.append(num[i])
        print(cos)
        return ''.join(cos[:-k or None]).lstrip('0')or "0"
        