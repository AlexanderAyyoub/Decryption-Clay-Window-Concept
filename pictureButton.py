from PyQt5.QtCore import QRect, QPoint
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QAbstractButton

class pictureButton(QAbstractButton):
    def __init__(self, pixmap, pixmap_hover, pixmap_pressed, parent=None):
        super(pictureButton, self).__init__(parent)
        self.pixmap = pixmap
        self.pixmap_hover = pixmap_hover
        self.pixmap_pressed = pixmap_pressed

        self.pressed.connect(self.update)
        self.released.connect(self.update)

    def paintEvent(self, event):
        pix = self.pixmap_hover if self.underMouse() else self.pixmap
        if self.isDown():
            pix = self.pixmap_pressed

        painter = QPainter(self)
        target_rect = self.rect()
        pixmap_rect = QRect(QPoint(0, 0), pix.size())  # Create QRect based on pixmap size
        painter.drawPixmap(target_rect, pix, pixmap_rect)
