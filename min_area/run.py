import math
from numpy import random
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

    _points = shape(xy_points)
    _points = _points[::-1]

    # Find minimum area bounding rectangle
    (rot_angle, area, width, height, center_point, corner_points) = min_bounding_rect(_points)

    print("Minimum area bounding box:")
    print("Width:", width, " Height:", height,)
 

