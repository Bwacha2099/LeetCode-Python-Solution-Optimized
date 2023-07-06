#URL: https://leetcode.com/problems/trapping-rain-water/

class Solution(object):
    def trap(self, height):
        """
        Calculate the amount of trapped rainwater.

        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n < 3:
            return 0
        
        left = 0
        right = n - 1
        left_max = height[left]
        right_max = height[right]
        water = 0

        while left < right:
            if height[left] <= height[right]:
                left_max = max(left_max, height[left])
                water += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                water += right_max - height[right]
                right -= 1
        
        return water
