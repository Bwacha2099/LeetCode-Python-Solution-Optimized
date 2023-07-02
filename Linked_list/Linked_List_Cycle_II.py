# Definition for singly-linked list.
# class ListNode(object):
# def __init__(self, x):
# self.val = x
# self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        Detects the starting node of a cycle in a linked list.

        :param head: The head of the linked list.
        :type head: ListNode
        :return: The starting node of the cycle, if exists; otherwise, None.
        :rtype: ListNode
        """
        if not head or not head.next:
            return None

        slow = head
        fast = head
        has_cycle = False

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                has_cycle = True
                break

        if not has_cycle:
            return None

        slow = head

        while fast != slow:
            fast = fast.next
            slow = slow.next

        return slow
