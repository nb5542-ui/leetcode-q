class Solution(object):
    def shiftingLetters(self, s, shifts):
        n = len(shifts)

        for i in range(n-2,-1,-1):
            shifts[i] += shifts[i + 1]

        ans = []
        for i in range(n):
            shift = shifts[i] % 26

            new_char = chr(
                (ord(s[i]) - ord('a') + shift) % 26 + ord('a')
            )
            ans.append(new_char)

        return "".join(ans)

        
        
        
        
        