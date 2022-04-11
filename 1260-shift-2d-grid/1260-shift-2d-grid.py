import numpy as np
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        initlen=len(grid[0])
        aa=np.array(grid)
        a=list(np.ndarray.flatten(aa))
        # print(a)
        k=k%len(a)
        for i in range(k):
            aaa=a.pop()
            a.insert(0,aaa)
        return np.reshape(a, (-1, initlen))
        