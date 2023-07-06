#URL: https://leetcode.com/problems/3sum-closest/

import sys


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        Find the sum of three numbers in nums that is closest to the target.

        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return 0

        nums.sort()
        closest_sum = float('inf')

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]

                if curr_sum == target:
                    return curr_sum

                if abs(curr_sum - target) < abs(closest_sum - target):
                    closest_sum = curr_sum

                if curr_sum < target:
                    left += 1
                else:
                    right -= 1

        return closest_sum


if __name__ == "__main__":
    soln = Solution()
    print(soln.threeSumClosest([-1, 2, 1, -4], 1))
    print(soln.threeSumClosest([-1, 2, 1, -4], 3))
