class Solution:
    def maxArea(self, h: List[int]) -> int:
        st=res=0
        width = en = len(h)-1
        for w in range(width,0,-1):
            if h[st]<h[en]:
                res=max(res,h[st]*w)
                st+=1
            else:
                res=max(res,h[en]*w)
                en-=1
        return res
        