class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store=set(nums)             #[100,4,200,1,3,2]
        res=0
        for num in nums:
            streak,cur=0,num
            if num-1 in store:
                continue
            while cur in store:
                streak+=1
                cur+=1
            res=max(res,streak)

        return res


