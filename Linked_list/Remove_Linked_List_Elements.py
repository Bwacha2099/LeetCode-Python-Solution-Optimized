# Definition for singly-linked list.
# class ListNode(object):
# def __init__(self, x):
# self.val = x
# self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head
        
        while current:
            if current.val == val:
                prev.next = current.next
            else:
                prev = current
            current = current.next
        
        return dummy.next
