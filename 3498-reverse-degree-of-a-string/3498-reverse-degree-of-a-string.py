class Solution(object):
    def reverseDegree(self, s):

        ans = 0

        for i in range(len(s)):

            ch = s[i]

            reverse_pos = ord('z') - ord(ch) + 1

            ans += reverse_pos * (i + 1)

        return ans













        


        