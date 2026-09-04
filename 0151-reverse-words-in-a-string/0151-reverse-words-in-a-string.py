class Solution(object):
    def reverseWords(self, s):
        words = s.split()
        right = len(words) - 1
        result = []

        while right >= 0:
            result.append(words[right])

            right -= 1

        return" ".join(result)

        



        
        