class Solution:
    def dfs(self,target,candy,path,tp):
        if target<0:
            return
        if target==0:
            tp.append(path)
            return
        for i in range(len(candy)):
            self.dfs(target-candy[i],candy[i:],path+[candy[i]],tp)
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret=[]
        self.dfs(target,candidates,[],ret)
        return ret