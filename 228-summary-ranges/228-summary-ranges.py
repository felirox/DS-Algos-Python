class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        op=[]
        s=0
        e=0
        while s<len(nums) and e<len(nums):
            if e+1<len(nums) and nums[e]+1==nums[e+1]:
                e+=1
            else:
                if s==e:
                    op.append(str(nums[s]))
                    s+=1
                    e+=1
                else:
                    op.append(str(nums[s])+"->"+str(nums[e]))
                    s=e+1
                    e+=1
        return op
            
            
        