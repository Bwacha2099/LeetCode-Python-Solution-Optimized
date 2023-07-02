# Definition for singly-linked list.
# class ListNode(object):
# def __init__(self, x):
# self.val = x
# self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        
        slow = head
        fast = head
        stack = []
        
        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        
        if fast:
            slow = slow.next
        
        while slow:
            if slow.val != stack.pop():
                return False
            slow = slow.next
        
        return True
