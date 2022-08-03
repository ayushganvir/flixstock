import math
from numpy import *
from min_rect import min_bounding_rect

from shape import shape

if __name__ == "__main__":
    # Square
    #xy_points = 10*array([(x,y) for x in arange(10) for y in arange(10)])

    # Random points
    xy_points = 10*random.random((32,2))
    print(xy_points)
    
    # A rectangle
    #xy_points = array([ [0,0], [1,0], [1,2], [0,2], [0,0] ])

    hull_points = shape(xy_points)
    hull_points = hull_points[::-1]
    print ('Convex hull points: \n', hull_points, "\n")

    # Find minimum area bounding rectangle
    (rot_angle, area, width, height, center_point, corner_points) = min_bounding_rect(hull_points)

    print("Minimum area bounding box:")
    print("Rotation angle:", rot_angle, "rad  (", rot_angle*(180/math.pi), "deg )")
    print("Width:", width, " Height:", height, "  Area:", area)
    print("Center point: \n", center_point )
    print("Corner points: \n", corner_points, "\n")


