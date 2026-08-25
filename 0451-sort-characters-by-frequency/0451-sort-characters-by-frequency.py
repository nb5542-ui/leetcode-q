class Solution(object):
    def frequencySort(self, s):
        
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch,0) + 1

        result = ""
        while freq:
            max_freq = max(freq.values())

            for ch in freq:
                if freq[ch] == max_freq:
                    result += ch * max_freq
                    del freq[ch]
                    break

        return result 
        
        
        