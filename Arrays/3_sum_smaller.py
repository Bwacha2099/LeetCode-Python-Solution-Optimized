# URL: https://leetcode.com/problems/3sum-smaller/

class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        Count the number of triplets in nums whose sum is less than target.

        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return 0

        triplet_count = 0
        sorted_nums = sorted(nums)
        n = len(sorted_nums)

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                curr_sum = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]

                if curr_sum < target:
                    # All triplets formed with the current right pointer will have a sum < target.
                    # So we count the number of valid triplets and move the left pointer forward.
                    triplet_count += right - left
                    left += 1
                else:
                    right -= 1

        return triplet_count


if __name__ == "__main__":
    soln = Solution()
    print(soln.threeSumSmaller([3, 1, 0, -2], 4))
