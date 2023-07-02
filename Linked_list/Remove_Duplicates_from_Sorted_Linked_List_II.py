# Definition for singly-linked list
# class ListNode(object):
# def __init__(self, x):
# self.val = x
# self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        
        dup_dict = {}
        current = head
        
        while current:
            if current.val in dup_dict:
                dup_dict[current.val] += 1
            else:
                dup_dict[current.val] = 1
            current = current.next
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head
        
        while current:
            if dup_dict[current.val] > 1:
                prev.next = current.next
            else:
                prev = current
            current = current.next
        
        return dummy.next
