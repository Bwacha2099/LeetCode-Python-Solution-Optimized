# Definition for singly-linked list.
# class ListNode(object):
# def __init__(self, x):
# self.val = x
# self.next = None


class Solution(object):
    def deleteNode(self, node):
        """
        Deletes the given node from a singly-linked list in-place.

        :param node: The node to be deleted.
        :type node: ListNode
        :return: None
        """
        if node is None:
            return

        next_node = node.next
        node.val = next_node.val
        node.next = next_node.next
