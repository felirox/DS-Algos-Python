class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        op=[]
        self.dfs(nums,[],op)
        return op
        
    def dfs(self,nums,pos,op):
        op.append(pos)
        for i in range(len(nums)):
            self.dfs(nums[i+1:],pos+[nums[i]],op)