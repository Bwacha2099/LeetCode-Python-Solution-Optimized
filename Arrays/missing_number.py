#URL: https://leetcode.com/problems/missing-number/

class Solution(object):
    def missingNumber(self, nums):
        """
        Find the missing number in the array.

        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        missing = n
        
        for i in range(n):
            missing ^= i ^ nums[i]
        
        return missing
