#URL: https://leetcode.com/problems/shortest-word-distance/

import sys

class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        Find the shortest distance between word1 and word2 in the list of words.

        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        min_dist = sys.maxsize
        prev_pos = None

        for i, word in enumerate(words):
            if word == word1 or word == word2:
                if prev_pos is not None and words[prev_pos] != word:
                    min_dist = min(min_dist, i - prev_pos)
                prev_pos = i

        return min_dist if min_dist != sys.maxsize else -1
