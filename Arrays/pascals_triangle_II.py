#URL: https://leetcode.com/problems/pascals-triangle-ii/

class Solution(object):
    def getRow(self, rowIndex):
        """
        Get the kth row of Pascal's triangle.

        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1] * (rowIndex + 1)
        
        for i in range(2, rowIndex + 1):
            for j in range(i - 1, 0, -1):
                row[j] += row[j - 1]
        
        return row
