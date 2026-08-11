class Solution(object):
    def hIndex(self, citations):

        citations.sort()

        n = len(citations)
        max_h = 0

        for i in range(n):

            if citations[i] == 0:
                continue

            count = len(citations[i:n])

            candidate = min(count, citations[i])

            max_h = max(max_h, candidate)

        return max_h