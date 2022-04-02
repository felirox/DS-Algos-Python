class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s[::-1]==s:
            return True
        st=0
        en=len(s)-1
        flex=0
        for i in range(len(s)):
            if s[st]!=s[en]:
                a=s[0:st]+s[st+1:]
                b=s[0:en]+s[en+1:]
                if a[::-1]==a or b[::-1]==b:
                    return True
                else:
                    return False
            st+=1
            en-=1
        return False