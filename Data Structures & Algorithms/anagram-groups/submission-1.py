class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)  #"apple":[] in default
        for s in strs:
            count=[0]*26
            for i in s:
                count[ord(i)-ord("a")]+=1
            res[tuple(count)].append(s)   #keys cannot be mutable, hence list -> tuple
        return list(res.values())
            