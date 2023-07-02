# Definition for singly-linked list.
# class ListNode(object):
# def __init__(self, x):
# self.val = x
# self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy
        slow = dummy
        
        # Move the fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next
        
        # Move both pointers until the fast pointer reaches the end
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        # Remove the nth node by modifying the next pointer
        slow.next = slow.next.next
        
        return dummy.next
