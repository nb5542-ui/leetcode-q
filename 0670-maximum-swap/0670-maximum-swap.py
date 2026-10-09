
class Solution(object):
    def maximumSwap(self, num):
        digits = list(str(num))
        n = len(digits)

        last = [0] * 10

        
        for i in range(n):
            last[int(digits[i])] = i

        
        for i in range(n):
            for d in range(9, int(digits[i]), -1):
                if last[d] > i:
                    j = last[d]
                    digits[i], digits[j] = digits[j], digits[i]
                    return int("".join(digits))

        return num

        
        