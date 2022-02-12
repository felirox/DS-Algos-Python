from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ds=Counter(s1)
        db=Counter(s2[:len(s1)-1])
        print(db)
        count=0
        for i in range(len(s1)-1,len(s2)):
            db[s2[i]]=db.get(s2[i],0)+1
            if db==ds:
                count+=1
            print("del",s2[i-len(s1)+1])
            print(db)
            db[s2[i-len(s1)+1]]-=1
            if db[s2[i-len(s1)+1]] ==0:
                del db[s2[i-len(s1)+1]]
                
        if count>0:
            return True
        else:
            return False