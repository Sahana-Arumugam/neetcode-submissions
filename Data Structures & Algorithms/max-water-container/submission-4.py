class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxh=0
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                maxh=max(maxh, min(heights[i],heights[j])*(j-i))



                # length=min(heights[i],heights[j])
                # breadth=j-i
                # area=length*breadth
                # maxh=max(area,maxh)
        return maxh