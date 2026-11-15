class Solution(object):
    def maxPoints(self, points):
        n = len(points)

        if n<= 2:      
            return n

        ans = 0
        for i in range(n):

            hashmap = {}
            duplicates = 1
            max_count = 1

            for j in range(i+1,n):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]

                if dx == 0 and dy == 0:
                    duplicates += 1
                    continue

                if dx == 0:
                    slope = (1,0)

                elif dy == 0:
                    slope = (0,1)

                else:
                    g = gcd(abs(dx),abs(dy))

                    dx //= g
                    dy //= g

                    if dx < 0:
                        dx = -dx
                        dy = -dy

                    slope = (dy, dx)

                hashmap[slope] = hashmap.get(slope, 0) + 1

                max_count = max(max_count, hashmap[slope])

            ans = max(ans, max_count + duplicates)

        return ans


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a    
                    


        
        