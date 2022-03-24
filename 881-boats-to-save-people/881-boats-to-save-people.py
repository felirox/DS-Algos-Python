from collections import defaultdict
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        b=0
        e=len(people)-1
        a=0
        people.sort()
        while b<=e:
            if people[b]+people[e]<=limit:
                b+=1
            a+=1
            e-=1
        return a
            
        