from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QDir
from PyQt5.QtGui import QImage
from ImagePlaylist import ImagePlaylist
from FuzzyDoodleUi import FuzzyDoodleUi


playerStyle = {'darkgray': '''
    QMainWindow { background-color: darkgray; }
    '''}


class FuzzyDoodlePlayer:

    def __init__(self):
        self.ui = FuzzyDoodleUi()
        self.initUi()

        # Initialize player features
        self.imageList = ImagePlaylist()
        self.playState = False

        # Inform user that we're ready for use
        self.ui.statusBar.showMessage('Ready!')

    def initUi(self):
        self.ui.setStyleSheet(playerStyle['darkgray'])

        self.ui.playPauseButton.clicked.connect(self.playPauseButtonAction)
        self.ui.backButton.clicked.connect(self.backButtonAction)
        self.ui.nextButton.clicked.connect(self.nextButtonAction)

        self.ui.importAction.triggered.connect(self.importFile)
        self.ui.importDirAction.triggered.connect(self.importDir)

    def playPauseButtonAction(self):
        imageCount = len(self.imageList)
        if imageCount > 0:
            self.playState = not(self.playState)
        else:
            self.playState = False

        if self.playState:
            self.ui.playPauseButton.setText('Pause')
            self.ui.nextButton.setEnabled(imageCount > 1)
            self.ui.backButton.setEnabled(self.imageList.hasHistory())

            self.ui.mainPictureWidget.enableBlurFade(False)

            if self.playState is False:
                self.loadImage(self.imageList.getImage())
                self.playState = True
        else:
            self.ui.playPauseButton.setText('Play')
            self.ui.backButton.setEnabled(False)
            self.ui.nextButton.setEnabled(False)
            self.ui.mainPictureWidget.enableBlurFade(True)

    def loadImage(self, imageFile):
        image = QImage(imageFile)
        self.ui.mainPicturePixmap.convertFromImage(image)

        print('PicturePixmap.size: '
              + str(self.ui.mainPicturePixmap.width())
              + ' x '
              + str(self.ui.mainPicturePixmap.height()))

        print('PictureLabel.size: '
              + str(self.ui.mainPictureWidget.width())
              + ' x '
              + str(self.ui.mainPictureWidget.height()))

        self.ui.mainPictureWidget.setPixmap(self.ui.mainPicturePixmap)
        self.ui.titleLabel.setText(imageFile)

    def backButtonAction(self):
        if len(self.imageList) <= 0 or self.playState is False:
            return

        self.loadImage(self.imageList.getPrevImage())

        hasHistory = self.imageList.hasHistory()
        self.ui.backButton.setEnabled(hasHistory)

    def nextButtonAction(self):
        if len(self.imageList) <= 0 or self.playState is False:
            return

        self.loadImage(self.imageList.getNextImage())

        hasHistory = self.imageList.hasHistory()
        self.ui.backButton.setEnabled(hasHistory)

    def importDir(self):
        dirName = QFileDialog.getExistingDirectory(
            self.ui, 'Open Directory', QDir.currentPath())

        print('dirName: ' + dirName)

        imported = self.imageList.appendDirectory(dirName)
        self.dispImportMsg(imported)

        if len(self.imageList) > 0:
            self.ui.playPauseButton.setEnabled(True)
            self.loadImage(self.imageList.getImage())

        print(self.imageList)

    def importFile(self):
        imageFile, _ = QFileDialog.getOpenFileName(
            self.ui, 'Open File', QDir.currentPath())

        imported = self.imageList.appendImage(imageFile)
        self.dispImportMsg(imported)

        if len(self.imageList) > 0:
            self.ui.playPauseButton.setEnabled(True)
            self.loadImage(self.imageList.getImage())

        print(self.imageList)

    def dispImportMsg(self, count):
        if count > 0:
            importMsg = 'Imported {0} images'.format(count)
        else:
            importMsg = 'No images imported.'
        self.ui.statusBar.showMessage(importMsg)
