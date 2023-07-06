#URL: https://leetcode.com/problems/plus-one/

class Solution(object):
    def plusOne(self, digits):
        """
        Add one to the number represented by the digits list.

        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        new_digits = []

        for digit in reversed(digits):
            running_sum = digit + carry
            carry = running_sum // 10
            new_digits.append(running_sum % 10)

        if carry == 1:
            new_digits.append(1)

        return new_digits[::-1]  # Reverse the list to get the correct order

