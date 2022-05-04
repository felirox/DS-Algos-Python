class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        #sorting the input so that we can implement two pointers in the same
        nums.sort()
        count=0
        
        # removing the numbers larger than k (since we need to make only pairs)
        while len(nums)>0 and nums[-1]>=k:
            nums.pop()
        if len(nums)==0:
            return 0
        l=0
        r=len(nums)-1
        
        #iterating and comparing if the least and the highest number equals to k
        #increment count if it's equal to k
        while l<r:
            if nums[l]+nums[r] ==k:
                nums.pop(r)
                nums.pop(l)
                r-=2
                count+=1
            #if it doesn't equal to 5, we need to move either of the pointer 
            #if the sum end up greater, then we exclude the max number
            #else, we exclude the min number
            elif nums[l]+nums[r] > k :
                r-=1
            else:
                l+=1
        return count