from math import sqrt, sin, cos, atan2, pi
from math import radians as rad
from math import degrees as deg


def distance(p1, p2):
    return sqrt((p2.x-p1.x)**2+(p2.y-p1.y)**2)


def step_pair(direc):
    return deg(sin(rad(direc))), deg(cos(rad(direc)))


def towards(p1, p2):
    delta_x = p2.x-p1.x
    delta_y = p2.y-p1.y

    if delta_y == 0:
        if delta_x < 0:
            return 90
        elif delta_x > 0:
            return 270
        else:
            return 0

    elif delta_x > 0:
        return 360 - deg(atan2(delta_y, delta_x)) % 360

    else:
        return 360 - (180+deg(atan2(delta_y, delta_x))) % 360


if __name__ == '__main__':
    from geometry import point
    tc = input('Test case: ')
    if tc == 'two points':
        ptup = [int(s.strip()) for s in input('First point: ').split(',')]
        p1 = point(ptup[0], ptup[1])
        ptup = [int(s.strip()) for s in input('Second point: ').split(',')]
        p2 = point(ptup[0], ptup[1])

        print(towards(p1, p2))

    elif tc == 'iter':
        p1 = point(0, 0)

        for x in range(-2, 2):
            x /= 2
            for y in range(-2, 2):
                y /= 2
                p2 = point(x, y)
                print('(0, 0) towards ('+str(x)+', '+str(y)+') = '+str(towards(p1, p2)))

