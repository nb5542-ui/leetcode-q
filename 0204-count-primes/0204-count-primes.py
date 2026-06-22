class Solution(object):
    def countPrimes(self, n):

        if n <= 2:
            return 0

        isPrime = [True] * n

        isPrime[0] = False
        isPrime[1] = False

        i = 2

        while i * i < n:

            if isPrime[i]:

                for multiple in range(i * i, n, i):
                    isPrime[multiple] = False

            i += 1

        return sum(isPrime)

        