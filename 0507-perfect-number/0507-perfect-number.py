class Solution(object):
    def checkPerfectNumber(self, num):

        if num == 1:
            return False

        divisorSum = 1

        i = 2

        while i * i <= num:

            if num % i == 0:

                divisorSum += i

                if i != num // i:
                    divisorSum += num // i

            i += 1

        return divisorSum == num
        