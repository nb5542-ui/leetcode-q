class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        from collections import Counter

        freq = Counter(barcodes)
        ordered = sorted(freq,key = lambda x: -freq[x])

        result = [0] * len(barcodes)
        i = 0

        for barcode in ordered:
            for _ in range(freq[barcode]):
                result[i] = barcode

                i += 2

                if i >= len(barcodes):
                    i = 1

        return result
       

                
        
        