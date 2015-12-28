import sys

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QFont, QImage
from PyQt5.QtCore import Qt, QRect, QRectF, QTimer

from entity import Entity


class Game(QWidget):
    def __init__(self):
        super().__init__()

        self.qp = QPainter()

        self.pi = 0
        self.entities = [
            Entity(0, 0, QImage.fromData(open('testsprites/hacker.png', 'rb').read(), format='png'), 45)
        ]
        self.player = self.entities[self.pi]

        self.timer = QTimer()
        self.pressed_buttons = set()

        self.qp = QPainter()

        self.mouse_x, self.mouse_y = 0, 0

        self.rect = None

        self.initUI()

    def initUI(self):
        self.timer.setInterval(50)
        self.timer.setTimerType(Qt.PreciseTimer)
        self.timer.timeout.connect(self.updaterender)
        self.timer.start()

        self.setGeometry(200, 200, 800, 800)

        self.setMouseTracking(True)

        self.show()

    def mouseMoveEvent(self, event):
        self.mouse_x = event.globalX()
        self.mouse_y = event.globalY()

    def paintEvent(self, event):
        self.rect = event.rect()

    def keyPressEvent(self, event):
        key = event.key()
        self.pressed.add(key)

    def keyReleaseEvent(self, event):
        key = event.key()
        if key in self.pressed:
            self.pressed.remove(key)

    def render_game(self):
        if self.rect and not self.paintingActive():
            print(self.qp.begin(self))
            self.qp.eraseRect(QRectF(self.rect))
            self.draw_entities(self.qp)
            self.qp.translate(400, 400)
            self.qp.drawImage(QRect(0, 0, 1000, 1000), QImage.fromData(open('testsprites/hacker.png', 'rb').read(),
                                                                     format='png'), self.rect)
            self.qp.end()

    def draw_entities(self, qp):
        for ent in self.entities:
            ent.draw(self, qp)

    def updaterender(self):
        self.render_game()
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gm = Game()
    exit(app.exec_())
