class Solution(object):
    def findMinArrowShots(self, points):
        
        points.sort(key=lambda x: x[1])

        
        arrows = 1
        arrow_position = points[0][1]

       
        for point in points[1:]:

           
            if point[0] > arrow_position:
                arrows += 1
                arrow_position = point[1]

        return arrows








        
        