# Definition for singly-linked list.
# class ListNode(object):
# def __init__(self, x):
# self.val = x
# self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        Merges two sorted linked lists into a single sorted linked list.

        :param l1: The head of the first linked list.
        :type l1: ListNode
        :param l2: The head of the second linked list.
        :type l2: ListNode
        :return: The head of the merged linked list.
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val <= l2.val:
            merged_head = l1
            l1 = l1.next
        else:
            merged_head = l2
            l2 = l2.next

        current = merged_head

        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        if l1:
            current.next = l1
        if l2:
            current.next = l2

        return merged_head
