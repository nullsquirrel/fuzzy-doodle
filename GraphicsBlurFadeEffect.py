from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGraphicsBlurEffect


class GraphicsBlurFadeEffect(QGraphicsBlurEffect):
    def __init__(self, parent):
        super().__init__(parent)
        self.setBlurRadius(32)
        self.setEnabled(True)

    def draw(self, painter):
        pixmap, offset = self.sourcePixmap()
        bounds = self.boundingRect()
        super().draw(painter)
        painter.save()
        painter.fillRect(bounds, QColor(128, 128, 128, 128))
        painter.restore()
