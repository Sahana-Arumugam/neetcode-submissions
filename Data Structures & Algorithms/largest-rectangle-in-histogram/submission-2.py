class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        maxarea=0
        for i,h in enumerate(heights):
            start=i
            while stack and stack[-1][1] > h:
                previ,prevh = stack.pop()
                maxarea=max(maxarea, prevh * (i - previ))
                start = previ
            stack.append([start,h])
        
        for i,h in stack:
            maxarea=max(maxarea , h * (len(heights) - i))
        return maxarea