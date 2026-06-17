class Solution(object):
    def getRow(self, rowIndex):
        row = [1]
        for i in range(rowIndex):
            curr = [1]
            for j in range(len(row) - 1):
                curr.append(row[j] + row[j + 1])

            curr.append(1)
            row = curr

        return row
        