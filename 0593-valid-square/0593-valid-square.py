class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        points = [p1,p2,p3,p4]
        distances = []
        for i in range(4):
            for j in range(i+1,4):
                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]

                distances.append(dx*dx + dy*dy)

        distances.sort()

        
        if distances[0] == 0:
            return False

        if not (distances[0] == distances[1] == distances[2] == distances[3]):
            return False

        
        if distances[4] != distances[5]:
            return False

        
        if distances[4] != 2 * distances[0]:
            return False

        return True


        