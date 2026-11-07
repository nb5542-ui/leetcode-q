from collections import Counter
class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        if  len(hand) % groupSize != 0:
            return False

        freq = Counter(hand)

        for card in sorted(hand):
            if freq[card] > 0:
                for num in range(card,card + groupSize):
                    if freq[num] == 0:
                        return False

                    freq[num] -= 1


        return True
        


        