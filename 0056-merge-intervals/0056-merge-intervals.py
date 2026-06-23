class Solution(object):
    def merge(self, intervals):

        intervals.sort()

        ans = [intervals[0]]

        for interval in intervals[1:]:

            if interval[0] <= ans[-1][1]:

                ans[-1][1] = max(ans[-1][1], interval[1])

            else:

                ans.append(interval)

        return ans