#Reverse a singly linked list.
#URL: https://leetcode.com/problems/reverse-linked-list/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head):
        """
        Reverses a singly-linked list.

        :param head: The head node of the linked list.
        :type head: ListNode
        :return: The new head of the reversed list.
        :rtype: ListNode
        """

        if head is None:
            return None

        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev
