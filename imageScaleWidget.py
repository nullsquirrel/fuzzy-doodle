from PyQt5 import QtCore
from PyQt5.QtWidgets import QLabel, QGraphicsBlurEffect, QGraphicsEffect

class ImageScaleWidget(QLabel):

    def __init__(self, parent):
        QLabel.__init__(self, parent)

        self.blurEffect = QGraphicsBlurEffect(self)
        self.blurEffect.setBlurRadius(10)
        self.blurEffect.setEnabled(True)
        self.setGraphicsEffect(self.blurEffect)

    def setPixmap(self, pixmap):
        self.pixmapOriginal = pixmap
        super(ImageScaleWidget, self).setPixmap(self.scaledPixmap())

    def resizeEvent(self, event):
        super(ImageScaleWidget, self).setPixmap(self.scaledPixmap())

    def scaledPixmap(self):
        return self.pixmapOriginal.scaled(self.size(), QtCore.Qt.KeepAspectRatio)

    def enableBlur(self, state):
        return self.blurEffect.setEnabled(state)

    def isBlurEnabled(self):
        return self.blurEffect.isEnabled()
