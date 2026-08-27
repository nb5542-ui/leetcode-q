from collections import Counter
class Solution(object):
    def lexGreaterPermutation(self, s, target):

        freq = Counter(s)
        ans = []
        for i in range(len(s)):
            if freq[target[i]] > 0:
                ans.append(target[i])
                freq[target[i]] -= 1

            else:
                for ch in sorted(freq):
                    if freq[ch] > 0 and ch > target[i]:
                        ans.append(ch)
                        freq[ch] -= 1

                        for c in sorted(freq):
                            ans.extend([c] * freq[c])

                        return ''.join(ans)

                break
        for i in range(len(ans)-1,-1,-1):
            freq[ans[i]] += 1

            for ch in sorted(freq):
                if freq[ch] > 0 and ch > target[i]:
                    result  = ans[:i] + [ch]
                    freq[ch] -= 1

                    for c in sorted(freq):
                        result.extend([c]*freq[c])

                    return ''.join(result)

        return ""

            
        
        