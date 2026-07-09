class Solution(object):
    def countGoodSubstrings(self, s):
        count = 0
        for i in range (len(s)-2):
            freq = {}
            for j in range(i,i+3):
                freq[s[j]] = freq.get(s[j],0)+1
            good = True

            for value in freq.values():
                if value > 1:
                    good = False
                    break
            if good:
                count += 1
        return count

        
        