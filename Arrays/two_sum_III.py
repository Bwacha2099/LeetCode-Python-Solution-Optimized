#URL: https://leetcode.com/problems/two-sum-iii-data-structure-design/

import collections

class TwoSum:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num_list = collections.defaultdict(int)

    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: None
        """
        self.num_list[number] += 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        if len(self.num_list) == 0:
            return False

        for num in self.num_list:
            target = value - num
            if (target in self.num_list and
                    (num != target or self.num_list[target] > 1)):
                return True

        return False

if __name__ == "__main__":
    # Your TwoSum object will be instantiated and called as such:
    twoSum = TwoSum()
    twoSum.add(0)
    twoSum.add(0)
    print(twoSum.find(0))
