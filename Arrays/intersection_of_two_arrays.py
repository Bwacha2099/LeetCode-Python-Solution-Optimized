#URL: https://leetcode.com/problems/intersection-of-two-arrays/

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        Find the intersection of two lists.

        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = set(nums1)
        nums2 = set(nums2)
        intersection = nums1.intersection(nums2)
        return list(intersection)
