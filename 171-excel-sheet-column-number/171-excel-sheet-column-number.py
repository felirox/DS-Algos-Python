class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        columnTitle=columnTitle[::-1]
        tot=0
        for i,j in enumerate(columnTitle):
            tot+=(ord(j)-64)*(26**i)
        return tot