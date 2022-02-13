class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        dt=Counter(nums)
        op=[]
        for i in nums:
            #print(i)
            dt[i]-=1
            tp=1
            #print("dt=",dt)
            if dt[i]==0:
                del dt[i]
            #print("del dt=",dt)
            for t in dt.keys():
                #print(t,dt[t],tp)
                tp*=t**dt[t]
            #print(tp)
            op.append(tp)
            #print("hmm",dt,i)
            if i not in dt: 
                dt[i]=1
            else:
                dt[i]+=1
            #print("post dt",dt)
        #print(op)
        return op
                