#URL: https://leetcode.com/problems/kth-largest-element-in-an-array/

import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        Find the kth largest element in an unsorted array.

        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Create a min heap with the first k elements
        min_heap = nums[:k]
        heapq.heapify(min_heap)

        # Process the remaining elements
        for i in range(k, len(nums)):
            if nums[i] > min_heap[0]:
                heapq.heapreplace(min_heap, nums[i])

        # The root of the min heap will be the kth largest element
        return min_heap[0]
