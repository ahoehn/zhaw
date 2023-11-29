import math


def find_closest_point(all_points,p):
    xp, yp = p  # unpacking tuple
    min_dist = 1e10  # something large
    for xi, yi in all_points:  # unpacking tuple
        dist = math.sqrt((xp-xi)**2 + (yp-yi)**2)
    if dist < min_dist:
        min_dist = dist
    min_p = (xi,yi)  # packing tuple
    return min_p, min_dist


print('closest', find_closest_point([(1, 4), (2, 9), (3, 1), (4, 7)], (2, 6)))
