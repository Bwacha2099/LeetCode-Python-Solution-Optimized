#URL: https://leetcode.com/problems/merge-k-sorted-lists/

import heapq

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        Merge k sorted linked lists into one sorted linked list.

        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None

        # Remove empty or None lists
        lists = [lst for lst in lists if lst]

        if not lists:
            return None

        heap = []
        for i, lst in enumerate(lists):
            heapq.heappush(heap, (lst.val, i, lst))

        dummy = ListNode(0)
        current = dummy

        while heap:
            _, i, node = heapq.heappop(heap)
            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next
