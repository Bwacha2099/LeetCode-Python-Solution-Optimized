#URL: https://leetcode.com/problems/rotate-array/

class Solution(object):
    def rotate(self, nums, k):
        """
        Rotate the input list by k positions in-place.

        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  # Normalize k if it's larger than n
        if k == 0 or n < 2:
            return  # No rotation needed
        
        self.reverse(nums, 0, n-1)  # Reverse the entire list
        self.reverse(nums, 0, k-1)  # Reverse the first k elements
        self.reverse(nums, k, n-1)  # Reverse the remaining elements

    def reverse(self, nums, start, end):
        """
        Reverse the elements in the input list between the start and end indices (inclusive).
        """
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


if __name__ == "__main__":
    soln = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7]
    soln.rotate(nums, 3)
    print(nums)
