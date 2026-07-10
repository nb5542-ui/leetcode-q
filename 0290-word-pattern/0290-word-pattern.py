class Solution(object):
    def wordPattern(self, pattern, s):

        words = s.split()

        if len(pattern) != len(words):
            return False

        pattern_to_word = {}
        word_to_pattern = {}

        for p, w in zip(pattern, words):

            if p in pattern_to_word:

                if pattern_to_word[p] != w:
                    return False

            else:
                pattern_to_word[p] = w

            if w in word_to_pattern:

                if word_to_pattern[w] != p:
                    return False

            else:
                word_to_pattern[w] = p

        return True
        