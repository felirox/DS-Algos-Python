class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        e=0
        o=len(nums)-1
        while e<=o:
            if nums[e]%2==0:
                e+=1
            else:
                nums[e],nums[o]=nums[o],nums[e]
                o-=1
        return nums
            
        