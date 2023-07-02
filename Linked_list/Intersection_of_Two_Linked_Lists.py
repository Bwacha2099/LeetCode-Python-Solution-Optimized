# Definition for singly-linked list.
# class ListNode(object):
# def __init__(self, x):
# self.val = x
# self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        Finds the intersection node of two linked lists.

        :param headA: The head of the first linked list.
        :type headA: ListNode
        :param headB: The head of the second linked list.
        :type headB: ListNode
        :return: The intersection node, if exists; otherwise, None.
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        lenA = self.getLength(headA)
        lenB = self.getLength(headB)

        diff = abs(lenA - lenB)

        if lenA > lenB:
            longer = headA
            shorter = headB
        else:
            longer = headB
            shorter = headA

        # Move the pointer of the longer list ahead by the difference
        for _ in range(diff):
            longer = longer.next

        # Traverse both lists together until an intersection node is found
        while longer and shorter:
            if longer == shorter:
                return longer
            longer = longer.next
            shorter = shorter.next

        return None

    def getLength(self, head):
        """
        Calculates the length of a linked list.

        :param head: The head of the linked list.
        :type head: ListNode
        :return: The length of the linked list.
        :rtype: int
        """
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        return length
