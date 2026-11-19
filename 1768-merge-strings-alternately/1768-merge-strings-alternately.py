class Solution(object):
    def mergeAlternately(self, word1, word2):

        total = len(word1) + len(word2)
        result = [""] * total

        i = 0
        while i < min(len(word1),len(word2)):

            result[2*i] = word1[i]
            result[2*i+1] = word2[i]

            i += 1

        pos = 2*i

        while i < len(word1):
            result[pos] = word1[i]
            pos += 1
            i += 1

        i = min(len(word1), len(word2))

        while i < len(word2):
            result[pos] = word2[i]
            pos += 1
            i += 1

        return "".join(result)

        


        



        
        
        