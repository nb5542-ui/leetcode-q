class Solution(object):
    def convertToTitle(self, columnNumber):

        ans = ""

        while columnNumber > 0:

            columnNumber -= 1

            remainder = columnNumber % 26

            ans = chr(ord('A') + remainder) + ans

            columnNumber //= 26

        return ans