#URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution(object):
    def removeDuplicates(self, nums):
        """
        Remove duplicates from the sorted list nums and return the length of the modified list.

        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)

        j = 0
        for i in range(1, len(nums)):
            if nums[j] != nums[i]:
                j += 1
                nums[j] = nums[i]

        return j + 1
