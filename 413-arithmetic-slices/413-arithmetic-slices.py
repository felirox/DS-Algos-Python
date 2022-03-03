class Solution:         
            
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        count=0
        listy=[0]*len(nums)
        for i in range(2,len(nums)):
            if nums[i-2]-nums[i-1]==nums[i-1]-nums[i]:
                listy[i]=listy[i-1]+1
            count+=listy[i]
        return count
        