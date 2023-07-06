#URL: https://leetcode.com/problems/maximum-subarray/

class Solution(object):
    def maxSubArray(self, nums):
        """
        Find the contiguous subarray with the largest sum.

        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        max_sum = float('-inf')  # Initialize with negative infinity
        curr_sum = 0

        for num in nums:
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)

        return max_sum
