class Solution(object):
    def numDecodings(self, s):
        n = len(s)
        dp = {}
        def ways(i):
            if i == n:
                return 1

            if s[i] == '0':
                return 0

            if i in dp:
                return dp[i]

            ans = ways(i + 1)

            if i + 1 < n:
                num = int(s[i:i+2])

                if 10 <= num <= 26:
                    ans += ways(i + 2)

            dp[i] = ans
            return ans
        return ways(0)
        
        