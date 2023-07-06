#URL: https://leetcode.com/problems/reverse-vowels-of-a-string/

class Solution(object):
    def __init__(self):
        self.__vowels = set("aeiouAEIOU")

    def reverseVowels(self, s):
        """
        Reverse the vowels in a string.

        :type s: str
        :rtype: str
        """
        if s is None or len(s) <= 1:
            return s
        
        s = list(s)
        i, j = 0, len(s) - 1

        while i < j:
            if s[i] not in self.__vowels:
                i += 1
                continue
            if s[j] not in self.__vowels:
                j -= 1
                continue
            
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        
        return "".join(s)
