class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        op1=[int(i) for i in version1.split(".")]
        op2=[int(i) for i in version2.split(".")]
        
        if len(op1)<len(op2):
            op1=op1+[0]*(len(op2)-len(op1))
        else:
            op2=op2+[0]*(len(op1)-len(op2))

        return (op1>op2)-(op2>op1)

            