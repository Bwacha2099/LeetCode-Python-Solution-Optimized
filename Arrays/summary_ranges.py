#URL: https://leetcode.com/problems/summary-ranges/

class Solution(object):
    def summaryRanges(self, nums):
        """
        Return the summary of ranges in a sorted integer array.

        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []

        ranges = []
        start = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                ranges.append(self.formatRange(start, nums[i - 1]))
                start = nums[i]

        ranges.append(self.formatRange(start, nums[-1]))

        return ranges

    def formatRange(self, start, end):
        """
        Format the range as a string.

        :type start: int
        :type end: int
        :rtype: str
        """
        if start == end:
            return str(start)
        else:
            return str(start) + "->" + str(end)
