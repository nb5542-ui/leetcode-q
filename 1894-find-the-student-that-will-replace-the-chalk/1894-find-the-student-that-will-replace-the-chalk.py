
class Solution(object):
    def chalkReplacer(self, chalk, k):

        total = sum(chalk)
        k = k % total

        i = 0

        while k >= chalk[i]:
            k -= chalk[i]
            i += 1

        return i