class Solution(object):
    def nthSuperUglyNumber(self, n, primes):

        k = len(primes)

        dp = [1] * n

        index = [0] * k

        for i in range(1, n):

            candidates = []

            for j in range(k):
                candidates.append(primes[j] * dp[index[j]])

            nextUgly = min(candidates)

            dp[i] = nextUgly

            for j in range(k):
                if candidates[j] == nextUgly:
                    index[j] += 1

        return dp[-1]

        