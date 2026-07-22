class Solution(object):
    def maxProduct(self, words):
        n = len(words)
        masks = []

        for word in words:
            mask = 0
            for ch in word:
                bit = ord(ch) - ord('a')

                mask |= (1 << bit)
            masks.append(mask)

        ans = 0
        for i in range(n):
            for j in range(i+1,n):
                if masks[i] & masks[j] == 0:
                    ans = max(
                        ans,
                        len(words[i])*len(words[j])

                    )

        return ans

        
        