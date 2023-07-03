#URL: https://leetcode.com/problems/3sum/

class Solution(object):
    def threeSum(self, nums):
        """
        Find all unique triplets in nums that sum up to zero.

        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []

        nums.sort()
        triplets = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]

                if curr_sum == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif curr_sum < 0:
                    left += 1
                else:
                    right -= 1

        return triplets


if __name__ == "__main__":
    soln = Solution()
    print(soln.threeSum([-1, 0, 1, 2, -1, -4]))
