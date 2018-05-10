from PyQt5 import QtCore
from PyQt5.QtWidgets import QLabel
from GraphicsBlurFadeEffect import GraphicsBlurFadeEffect

class ImageScaleWidget(QLabel):

    def __init__(self, parent):
        QLabel.__init__(self, parent)

        self.blurFadeEffect = GraphicsBlurFadeEffect(self)
        self.blurFadeEffect.setBlurRadius(64)
        self.blurFadeEffect.setEnabled(True)
        self.setGraphicsEffect(self.blurFadeEffect)

    def setPixmap(self, pixmap):
        self.pixmapOriginal = pixmap
        super(ImageScaleWidget, self).setPixmap(self.scaledPixmap())

    def resizeEvent(self, event):
        super(ImageScaleWidget, self).setPixmap(self.scaledPixmap())

    def scaledPixmap(self):
        return self.pixmapOriginal.scaled(self.size(), QtCore.Qt.KeepAspectRatio)

    def enableBlurFade(self, state):
        return self.blurFadeEffect.setEnabled(state)

    def isBlurFadeEnabled(self):
        return self.blurFadeEffect.isEnabled()
