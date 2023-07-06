#URL: https://leetcode.com/problems/majority-element/

class Solution(object):
    def majorityElement(self, nums):
        """
        Find the majority element in the list nums.

        :type nums: List[int]
        :rtype: int
        """
        candidate = self.get_candidate(nums)
        count = 0
        for num in nums:
            if num == candidate:
                count += 1

        return candidate if count > len(nums) // 2 else None

    def get_candidate(self, nums):
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        return candidate
