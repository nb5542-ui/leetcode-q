class Solution(object):
    def reorganizeString(self, s):

        freq = {}

        for ch in s:
            if ch not in freq:
                freq[ch] = 1
            else:
                freq[ch] += 1

        max_char = max(freq, key=freq.get)

        if freq[max_char] > (len(s) + 1) // 2:
            return ""

        result = [''] * len(s)

        index = 0

        
        for _ in range(freq[max_char]):
            result[index] = max_char
            index += 2

            if index >= len(s):
                index = 1

        
        for ch in freq:
            if ch == max_char:
                continue

            for _ in range(freq[ch]):
                result[index] = ch
                index += 2

                if index >= len(s):
                    index = 1

        return ''.join(result)
        

        
        