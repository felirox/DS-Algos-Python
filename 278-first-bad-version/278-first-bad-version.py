# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l=1
        r=n
        first=-1
        while l<=r:
            m=(l+r)//2
            if isBadVersion(m)==True:
                r=m-1
                first=m
            elif isBadVersion(m)==False:
                l=m+1
        return first
        
        