class Solution(object):
    def isIsomorphic(self, s, t):
        """
        Determines if two input strings are isomorphic.

        :param s: The first input string.
        :type s: str
        :param t: The second input string.
        :type t: str
        :return: True if the strings are isomorphic, False otherwise.
        :rtype: bool
        """
        if s is None or t is None:
            return False

        if len(s) != len(t):
            return False

        mapping_s = {}
        mapping_t = {}

        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]

            if char_s in mapping_s:
                if mapping_s[char_s] != char_t:
                    return False
            else:
                mapping_s[char_s] = char_t

            if char_t in mapping_t:
                if mapping_t[char_t] != char_s:
                    return False
            else:
                mapping_t[char_t] = char_s

        return True
