class Solution(object):
    def nthUglyNumber(self, n):

        ugly = [1]

        p2 = 0
        p3 = 0
        p5 = 0

        while len(ugly) < n:

            next2 = ugly[p2] * 2
            next3 = ugly[p3] * 3
            next5 = ugly[p5] * 5

            nextUgly = min(next2, next3, next5)

            ugly.append(nextUgly)

            if nextUgly == next2:
                p2 += 1

            if nextUgly == next3:
                p3 += 1

            if nextUgly == next5:
                p5 += 1

        return ugly[-1]