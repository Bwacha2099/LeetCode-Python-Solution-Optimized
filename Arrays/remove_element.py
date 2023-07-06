#URL: https://leetcode.com/problems/remove-element/

class Solution(object):
    def removeElement(self, nums, val):
        """
        Remove all occurrences of the specified value from the list.

        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        
        return i
