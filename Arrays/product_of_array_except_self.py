#URL: https://leetcode.com/problems/product-of-array-except-self/

class Solution(object):
    def productExceptSelf(self, nums):
        """
        Find the product of all elements except self.

        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        product = [0] * n
        product[0] = 1

        # Calculate the product of elements to the left of each index
        for i in range(1, n):
            product[i] = product[i-1] * nums[i-1]

        # Calculate the product of elements to the right of each index and multiply it with the previously calculated left product
        right_product = 1
        for i in range(n-1, -1, -1):
            product[i] *= right_product
            right_product *= nums[i]

        return product
