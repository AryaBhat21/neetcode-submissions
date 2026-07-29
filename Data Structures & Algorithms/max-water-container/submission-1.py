class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        area = 0 
        while left<right:
            height = min(heights[left],heights[right])
            width = left+right
            area = max(area, (height*width))
            left+=1
            right-=1


        return area