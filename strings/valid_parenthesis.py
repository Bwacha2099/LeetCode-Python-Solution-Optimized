class Solution:
    def isValid(self, s: str) -> bool:
        """
        Checks if a given string has valid pairing and nesting of parentheses, curly brackets, and square brackets.

        :param s: The input string to be checked.
        :type s: str
        :return: True if the string is valid, False otherwise.
        :rtype: bool
        """
        stack = []
        openings = "({["
        closings = ")}]"
        for symbol in s:
            if symbol in openings:
                stack.append(symbol)
            elif symbol in closings:
                if not stack:
                    return False
                top = stack.pop()
                if openings.index(top) != closings.index(symbol):
                    return False
        return not stack
