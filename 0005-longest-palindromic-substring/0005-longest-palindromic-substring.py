class Solution:
    def longestPalindrome(self, s): 

        n = len(s)

        dp = [[False] * n for _ in range(n)]

        start = 0
        maxLength = 1

       
        for i in range(n):
            dp[i][i] = True

        
        for length in range(2, n + 1):

            for left in range(n - length + 1):

                right = left + length - 1

                if s[left] == s[right]:

                    if length == 2:
                        dp[left][right] = True

                    else:
                        dp[left][right] = dp[left + 1][right - 1]

                    if dp[left][right] and length > maxLength:
                        start = left
                        maxLength = length

        return s[start:start + maxLength]