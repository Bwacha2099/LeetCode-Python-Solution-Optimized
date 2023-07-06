#URL: https://leetcode.com/problems/contains-duplicate-ii/

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        Check if there are any duplicate elements within a range of k indices in the list nums.

        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        index_dict = {}

        for i, num in enumerate(nums):
            if num in index_dict and i - index_dict[num] <= k:
                return True
            index_dict[num] = i

        return False
