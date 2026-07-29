class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(nums)-1
        area = 0 
        while left<right:
            height = min(nums[left],nums[right])
            width = left+right+1
            area = max(area, (height*width))

        return area