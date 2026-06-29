class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        sh,th={},{}
        for i in range(len(s)):
            sh[s[i]]=1+sh.get(s[i],0)
            th[t[i]]=1+th.get(t[i],0)
        
        for j in sh:
            if sh[j]!=th.get(j,0):
                return False
        
        return True
