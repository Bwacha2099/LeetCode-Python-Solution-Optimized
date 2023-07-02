import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Checks if a given string is a palindrome.

        :param s: The input string to be checked.
        :type s: str
        :return: True if the string is a palindrome, False otherwise.
        :rtype: bool
        """
        s = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
        return s == s[::-1]
