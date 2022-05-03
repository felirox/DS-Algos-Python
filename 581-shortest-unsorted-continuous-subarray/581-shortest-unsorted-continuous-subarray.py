class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        start=0
        end=len(nums)-1
        if len(nums)<2:
            return 0
        while start<end and nums[start]<=nums[start+1]:
            start+=1
        while end>0 and nums[end]>=nums[end-1]:
            end-=1
        if start>end:
            return 0
        minn=min(nums[start:end+1])
        maxx=max(nums[start:end+1])
        while start>0 and minn<nums[start-1]:
            start-=1
        while end<len(nums)-1 and maxx>nums[end+1]:
            end+=1
        return end-start+1
        
        
        