class Solution:
    def dfs(self,tar,candy,cp,tp):
        if tar<0:
            return
        if tar==0:
            tp.append(cp)
            return
        if len(cp)>150:
            return
        for i in range(len(candy)):
            self.dfs(tar-candy[i],candy[i:],cp+[candy[i]],tp)
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        tp=[]
        self.dfs(target,candidates,[],tp)
        return tp
        