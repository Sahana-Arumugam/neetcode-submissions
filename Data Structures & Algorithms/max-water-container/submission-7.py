class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        area=0
        while l<r:
            area=max(area,(min(heights[l],heights[r])*(r-l)))
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return area





 #Brute Force
#class Solution:
    # def maxArea(self, heights: List[int]) -> int:
    #     maxh=0
    #     for i in range(len(heights)):
    #         for j in range(i+1,len(heights)):
    #             length=min(heights[i],heights[j])
    #             breadth=j-i
    #             area=length*breadth
    #             maxh=max(area,maxh)
    #     return maxh