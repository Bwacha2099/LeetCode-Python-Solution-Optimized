#URL: https://leetcode.com/problems/nested-list-weight-sum/

class Solution(object):
    def depthSum(self, nestedList):
        """
        Calculate the weighted sum of integers in the nestedList.

        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        return self.depthSumHelper(nestedList, 1)

    def depthSumHelper(self, nested_list, depth):
        if not nested_list:
            return 0

        total_sum = 0
        for entry in nested_list:
            if entry.isInteger():
                total_sum += entry.getInteger() * depth
            else:
                total_sum += self.depthSumHelper(entry.getList(), depth + 1)

        return total_sum
