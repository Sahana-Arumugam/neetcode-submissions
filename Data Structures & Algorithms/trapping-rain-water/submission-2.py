class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0,len(height)-1
        leftMax , rightMax = height[l],height[r]
        cap=0
        while l<r:
            if leftMax < rightMax:
                l+=1
                leftMax=max(leftMax, height[l])
                cap+= leftMax - height[l]

            else:
                r-=1
                rightMax=max(rightMax, height[r])
                cap+= rightMax - height[r]
        return cap