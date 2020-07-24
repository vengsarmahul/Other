#Closet Distance of the XY Coordinates

import math


n = int(input('Please enter the number of coordinate to compare: '))


def distance(coord):
    distance = []
    n = 0
    for point in coord:
        while n != len(point)-1:
            n = n + 1
            x = point[0] - point[n]
            distance.append(x**2)
        return [distance]
    

def minimum(coordx,coordy):
    squr = []
    n = 0
    for point in coordx:
        total = math.sqrt(point[0] + coordy[0][0])
        squr.append(round(total,2))
        while n != len(point)-1:
            n = n + 1
            total = math.sqrt(point[n] + coordy[0][n])
            squr.append(round(total,2))
        minimum = min(squr)
    return minimum


coord = []

for n in range(0,n):
    x = (float(input('Enter X value: ')),float(input('Enter Y value: ')))
    coord.append(tuple(x))
    
y = sorted(coord, key = lambda coord: coord[0])

midvalue = round(len(y)/2)
mid_coord_left = midvalue - 1
mid_coord_right = midvalue + 1

left = y[:midvalue]
right = y[midvalue:]
mid_coords_total = y[mid_coord_left:midvalue]  + y[midvalue:mid_coord_right]

leftX = [[point[0] for point in left]]
leftY = [[point[1] for point in left]]
rightX = [[point[0] for point in right]]
rightY = [[point[1] for point in right]]
mid_coordX = [[point[0] for point in mid_coords_total]]
mid_coordY = [[point[1] for point in mid_coords_total]]

leftXvalues = distance(leftX)
leftYvalues = distance(leftY)
rightXvalues = distance(rightX)
rightYvalues = distance(rightY)
midXvalues = distance(mid_coordX)
midYvalues = distance(mid_coordY)

min_dist_left = minimum(leftXvalues,leftYvalues)
min_dist_right = minimum(rightXvalues,rightYvalues)

min_dist_Mid = minimum(midXvalues,midYvalues)
min_dist_LR = min(min_dist_left,min_dist_right)


print('In the collection of coordinates {}' .format(y))
print('The minimum distance is: {}' .format(min(min_dist_LR, min_dist_Mid)))
