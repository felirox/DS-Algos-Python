class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stk=[]
        io=0
        for i in pushed:
            stk.append(i)
            while stk and popped[io]==stk[-1]:
                stk.pop()
                io+=1
        print(stk)   
        return len(stk)==0
        