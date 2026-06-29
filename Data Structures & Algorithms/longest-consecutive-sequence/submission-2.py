class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store=set(nums)
        res=0
        for n in nums:
            streak,length=0,0
            if (n-1) not in store:
                while (n+length) in store:
                    length+=1
                res=max(res,length)
        return res






# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         store=set(nums)             #[100,4,200,1,3,2]
#         res=0
#         for num in nums:
#             streak,cur=0,num
#             if num-1 in store:
#                 continue
#             while cur in store:
#                 streak+=1
#                 cur+=1
#             res=max(res,streak)

#         return res