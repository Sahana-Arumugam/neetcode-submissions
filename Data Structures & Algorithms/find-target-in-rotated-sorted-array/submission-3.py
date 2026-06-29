class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l,r = 0,len(nums)-1

        while l<=r:
            m=(l+r)//2

            if nums[m]==target:
                return m
            
            #left sorted
            if nums[l]<=nums[m]:
                if target < nums[l] or target > nums[m]:  #if target is not in the left sorted 
                    l=m+1
                else:       #target in left, ignore right part
                    r=m-1
            #right sorted
            else:
                if target >nums[r] or target < nums[m]:   #if target is not in the right sorted 
                    r=m-1
                else:
                    l=m+1
            
        return -1
