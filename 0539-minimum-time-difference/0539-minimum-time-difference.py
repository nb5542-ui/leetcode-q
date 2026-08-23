class Solution(object):
    def findMinDifference(self, timePoints):
        minutes = []
        for time in timePoints:
            hour = int(time[0:2])
            minute = int(time[3:5])

            minutes.append(hour*60 + minute)

        minutes.sort()
        min_diff = float('inf')

        for i in range(1,len(minutes)):
            diff = minutes[i] - minutes[i-1]
            min_diff = min(min_diff,diff)

        wrap_diff = 1440 - minutes[-1] + minutes[0]
        min_diff = min(min_diff,wrap_diff)

        return min_diff