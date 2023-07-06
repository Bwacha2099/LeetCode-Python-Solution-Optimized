#URL: https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        Find the intersection of two lists.

        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        sorted_nums1 = sorted(nums1)
        sorted_nums2 = sorted(nums2)
        intersect_list = []
        
        i, j = 0, 0
        
        while i < len(sorted_nums1) and j < len(sorted_nums2):
            if sorted_nums1[i] < sorted_nums2[j]:
                i += 1
            elif sorted_nums1[i] > sorted_nums2[j]:
                j += 1
            else:
                intersect_list.append(sorted_nums1[i])
                i += 1
                j += 1
        
        return intersect_list