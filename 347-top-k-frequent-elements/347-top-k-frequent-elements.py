from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        col=defaultdict(int)
        for i in nums:
            col[i]+=1
        ll=[max(col, key=col.get)]
        for _ in range(k-1):
            del col[ll[-1]]
            ll.append(max(col, key=col.get))
        return(ll)

        