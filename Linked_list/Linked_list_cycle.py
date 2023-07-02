#Given a linked list, determine if it has a cycle in it.
#URL: https://leetcode.com/problems/linked-list-cycle/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head):
        """
        Determines whether a singly-linked list has a cycle.

        :param head: The head node of the linked list.
        :type head: ListNode
        :return: True if the linked list contains a cycle, False otherwise.
        :rtype: bool
        """

        if head is None:
            return False

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
