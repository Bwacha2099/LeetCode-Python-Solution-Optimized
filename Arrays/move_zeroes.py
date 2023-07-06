#URL:https://leetcode.com/problems/move-zeroes/

class Solution(object):
    def moveZeroes(self, nums):
        """
        Move all the zeros in the list to the end, maintaining the relative order of non-zero elements.

        :type nums: List[int]
        :rtype: void
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1

        for j in range(i, len(nums)):
            nums[j] = 0
