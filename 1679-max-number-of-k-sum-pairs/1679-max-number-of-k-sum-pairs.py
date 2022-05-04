class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        count=0
        while len(nums)>0 and nums[-1]>=k:
            nums.pop()
        if len(nums)==0:
            return 0
        l=0
        r=len(nums)-1
        while l<r:
            tot=nums[l]+nums[r]
            if tot ==k:
                nums.pop(r)
                nums.pop(l)
                r-=2
                count+=1
            elif nums[l]+nums[r] > k :
                r-=1
            else:
                l+=1
        
        return count