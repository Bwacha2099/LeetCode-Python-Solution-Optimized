class Solution:
    def reverseString(self, s: str) -> str:
        """
        Reverses a given string.

        :param s: The input string to be reversed.
        :type s: str
        :return: The reversed string.
        :rtype: str
        """

        current_str = list(s)
        i, j = 0, len(s) - 1

        while i < j:
            current_str[i], current_str[j] = current_str[j], current_str[i]
            i += 1
            j -= 1

        return "".join(current_str)

solution = Solution()
result = solution.reverseString("hello")
print(result)  # Output: "olleh"
