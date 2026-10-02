class Solution(object):
    def totalFruit(self, fruits):
        i = 0
        freq = {}
        maximum = 0
        for j in range(len(fruits)):
            freq[fruits[j]] = freq.get(fruits[j],0) + 1

            while len(freq) > 2:
                freq[fruits[i]] -= 1

                if freq[fruits[i]] == 0:
                    del freq[fruits[i]]

                i += 1

            maximum = max(maximum,j-i+1)
        return maximum
        

        