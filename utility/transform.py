from geometry import point


def pos_transform(around, entity):
    return point(around.x+entity.x, around.y+entity.y)