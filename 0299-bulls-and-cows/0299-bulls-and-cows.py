class Solution(object):
    def getHint(self, secret, guess):

        bull = 0
        cow = 0
        freq = {}

        
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1

        
        for i in range(len(secret)):
            if secret[i] != guess[i]:
                freq[secret[i]] = freq.get(secret[i], 0) + 1

        
        for i in range(len(guess)):
            if secret[i] != guess[i]:
                if guess[i] in freq and freq[guess[i]] > 0:
                    cow += 1
                    freq[guess[i]] -= 1

        return str(bull) + "A" + str(cow) + "B"