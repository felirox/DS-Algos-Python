from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maxx=-1
        count=0
        
        for i in nums:
            if count==0:
                maxx=i
                count=1
            else:
                if maxx==i:
                    count+=1
                else:
                    count-=1
                    
        return maxx