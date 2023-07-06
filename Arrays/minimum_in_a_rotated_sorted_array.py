#URL: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution(object):
    def findMin(self, nums):
        """
        Find the minimum element in a rotated sorted array.

        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            # If the mid element is greater than the rightmost element,
            # the pivot is on the right side. Update the left pointer.
            if nums[mid] > nums[right]:
                left = mid + 1
            # If the mid element is less than or equal to the rightmost element,
            # the pivot is on the left side. Update the right pointer.
            else:
                right = mid

        return nums[left]
