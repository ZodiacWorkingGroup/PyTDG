from PyQt5.QtCore import QRect
from utility.transform import pos_transform


from geometry import *


class Entity:
    def __init__(self, x, y, sprite, rot=0):
        self.position = point(x, y)
        self.sprite = sprite
        self.rotation = rot

    def draw(self, game, qp):  # When called, draws its "sprite" attribute using qp. Qp should be a QPainter.
        if self is game.player:  # For a sprite which is the player (rendered in the centre of the window)
            geom = game.geometry()  # Get the size of the game window to find the centre
            sprite = self.sprite  # May be the problem (an empty image), but I would think that would raise an error
                                  # when the image is loaded
            r = self.rotation  # The rotation in degrees of the current sprite

            dx = 10*sprite.width()  # x-offset of opposing corner
            dy = 10*sprite.height()  # y-offset of opposing corner
            qp.save()  # Record the current transformation (at least, that's what it seems to do)
            qp.translate(geom.width()/2, geom.height()/2)  # Go to the center of the canvas
            # qp.rotate(r)  # Rotate the image accordingly

            rec = QRect(-dx/20, -dy/20, dx, dy)  # The area where the sprite should be drawn (I, frankly, have no clue
                                                 # why this is the way it is, but it worked in the other one I made)

            qp.drawImage(rec, sprite, game.rect)  # Draw the image on the game (game.rect is the rect() method of any
                                                  # paint event that occurs, to keep everything lined up)

            qp.restore()  # Revert the transformations so that subsequent drawings are in the right location

        else:  # For any other non-player sprite
            transformed = pos_transform(game.player.position, self.position)  # pos_transform is used for relative
                                                                              # positioning based on a fixed point
            x = transformed.x  # pos_transform returns a point with the attributes x and y
            y = transformed.y

            # From this point on, future code will only finish if the sprite falls in the game geometry, such as to be
            # more efficient
            sprite = self.sprite  # Again, a QImage
            r = self.rotation  # The rotation in degrees of the current sprite

            dx = 10*sprite.width()  # x-offset
            dy = 10*sprite.height()  # y-offset
            qp.save()  # Save transformation
            qp.translate(x, y)  # Go to the proper location
            # qp.rotate(r)  # Rotation

            rec = QRect(-dx/20, -dy/20, dx, dy)  # Still don't know why this works

            qp.drawImage(rec, sprite, game.rect)  # Draw the image

            qp.restore()  # Revert the transformations
