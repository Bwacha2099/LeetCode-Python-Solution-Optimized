#URL: https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums):
        """
        Check if the input list contains any duplicate elements.

        :type nums: List[int]
        :rtype: bool
        """
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)
        return False
