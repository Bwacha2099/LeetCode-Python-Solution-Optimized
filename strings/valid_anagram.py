from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Checks if two strings are anagrams of each other.

        :param s: The first input string.
        :type s: str
        :param t: The second input string.
        :type t: str
        :return: True if the strings are anagrams, False otherwise.
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        s_count = Counter(s)
        t_count = Counter(t)

        return s_count == t_count
