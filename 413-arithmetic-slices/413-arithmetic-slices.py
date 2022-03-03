class Solution:         
            
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        count=0
        prev=0
        curr=0
        for i in range(2,len(nums)):
            if nums[i-2]-nums[i-1]==nums[i-1]-nums[i]:
                curr=prev+1
            count+=curr
            prev=curr
            curr=0
        return count
        