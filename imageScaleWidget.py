from PyQt5 import QtCore
from PyQt5.QtWidgets import QLabel

class ImageScaleWidget(QLabel):

    def setPixmap(self, pixmap):
        self.pixmapOriginal = pixmap
        super(ImageScaleWidget, self).setPixmap(self.scaledPixmap())

    def resizeEvent(self, event):
        super(ImageScaleWidget, self).setPixmap(self.scaledPixmap())

    def scaledPixmap(self):
        return self.pixmapOriginal.scaled(self.size(), QtCore.Qt.KeepAspectRatio)
