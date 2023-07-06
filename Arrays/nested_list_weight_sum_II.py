#URL: https://leetcode.com/problems/nested-list-weight-sum-ii/

class Solution(object):
    def depthSumInverse(self, nestedList):
        """
        Calculate the weighted sum of integers in the nestedList.

        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        max_depth = self.getMaxDepth(nestedList)
        return self.getWeightedSum(nestedList, max_depth)

    def getMaxDepth(self, nested_list):
        if not nested_list:
            return 0

        max_depth = 1
        for entry in nested_list:
            if not entry.isInteger():
                max_depth = max(max_depth, self.getMaxDepth(entry.getList()) + 1)

        return max_depth

    def getWeightedSum(self, nested_list, depth):
        if not nested_list:
            return 0

        weighted_sum = 0
        for entry in nested_list:
            if entry.isInteger():
                weighted_sum += entry.getInteger() * depth
            else:
                weighted_sum += self.getWeightedSum(entry.getList(), depth - 1)

        return weighted_sum
