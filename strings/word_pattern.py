class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        Checks if a given pattern matches the words in a string.

        :param pattern: The pattern string to be checked.
        :type pattern: str
        :param s: The input string.
        :type s: str
        :return: True if the pattern matches the words, False otherwise.
        :rtype: bool
        """
        words = s.split()

        if len(pattern) != len(words):
            return False

        pattern_to_word = {}
        word_to_pattern = {}

        for p, w in zip(pattern, words):
            if p not in pattern_to_word and w not in word_to_pattern:
                pattern_to_word[p] = w
                word_to_pattern[w] = p
            elif pattern_to_word.get(p) != w or word_to_pattern.get(w) != p:
                return False

        return True
