class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        dt=Counter(nums)
        op=[]
        for i in nums:
            dt[i]-=1
            tp=1
            if dt[i]==0:
                del dt[i]
            for t in dt.keys():
                tp*=t**dt[t]
            op.append(tp)
            if i not in dt: 
                dt[i]=1
            else:
                dt[i]+=1
        return op
                