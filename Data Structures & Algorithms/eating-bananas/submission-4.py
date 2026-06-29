class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)
        res=r           #max no. of bananas we can eat in an hour, goal is to find the minimum
        while l<=r:
            k=(l+r)//2
            hrs=0
            for i in piles:
                hrs+=math.ceil(i / k)

            if hrs <= h:
                res=min(res,k)
                r=k-1
            else:
                l=k+1
        return res
                

