import sys, os
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import (QMainWindow, QFileDialog, QLabel, QGridLayout,
                             QAction, QHBoxLayout,
                             QPushButton, QSizePolicy, QWidget)
from PyQt5.QtCore import QDir, QSize
from PyQt5.QtGui import QPixmap, QImage
from ImageScaleWidget import ImageScaleWidget
from ImagePlaylist import ImagePlaylist


playerStyle = {'darkgray': '''
    QMainWindow { background-color: darkgray; }
    '''
}

class FuzzyDoodlePlayer(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        self.imageList = ImagePlaylist()
        self.imageIndex = -1
        self.playState = False
        self.setStyleSheet(playerStyle['darkgray'])

        # Initialize GUI
        self.initWindow()
        self.initMenuBar()
        self.initBody()

        # Inform user that we're ready for use
        self.statusBar().showMessage('Ready!')


    def initWindow(self):
        screenGeometry = QtWidgets.QApplication.desktop().screenGeometry()
        requestedSize = QSize(screenGeometry.width()*2/3,
                                screenGeometry.height()*2/3)
        self.setMinimumSize(320, 320)
        self.resize(requestedSize)
        self.setWindowTitle('Fuzzy Doodle Sketch Practice')


    def initBody(self):
        # Setup central grid layout
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        gridLayout = QGridLayout(self)
        centralWidget.setLayout(gridLayout)

        self.initPictureFrame()
        self.initBodyButtons()

        # Add widgets to layout
        gridLayout.addWidget(self.mainPictureWidget, 0, 0)
        gridLayout.addWidget(self.titleLabel, 1, 0)
        gridLayout.addLayout(self.buttonLayout, 2, 0)


    def initPictureFrame(self):
        # Create Title Label
        self.titleLabel = QLabel('Fuzzy Doodle Sketch Practice', self)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        # Create main image label
        self.mainPictureWidget = ImageScaleWidget(self)
        self.mainPicturePixmap = QPixmap()
        self.mainPictureWidget.setPixmap(self.mainPicturePixmap)
        self.mainPictureWidget.scaleFactor = 1.0
        self.mainPictureWidget.setAlignment(QtCore.Qt.AlignCenter)


    def initBodyButtons(self):
        # Create back button
        self.backButton = QPushButton('Back', self)
        self.backButton.setToolTip('Go to previous image')
        self.backButton.clicked.connect(self.backButtonAction)
        self.backButton.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.backButton.setEnabled(False)

        # Create pause/play button
        self.playPauseButton = QPushButton('Play', self)
        self.playPauseButton.setToolTip('Start/continue practice session')
        self.playPauseButton.clicked.connect(self.playPauseButtonAction)
        self.playPauseButton.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        # Create next button
        self.nextButton = QPushButton('Next', self)
        self.nextButton.setToolTip('Go to next image')
        self.nextButton.clicked.connect(self.nextButtonAction)
        self.nextButton.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.nextButton.setEnabled(False)

        # Create button widget
        self.buttonLayout = QHBoxLayout(self)
        self.buttonLayout.addWidget(self.backButton)
        self.buttonLayout.addWidget(self.playPauseButton)
        self.buttonLayout.addWidget(self.nextButton)


    def playPauseButtonAction(self):
        imageCount = len(self.imageList)
        if imageCount > 0:
            self.playState = not(self.playState)
        else:
            self.playState = False

        if self.playState:
            self.playPauseButton.setText('Pause')
            self.imageIndex = 0
            self.loadImage(self.imageList[self.imageIndex])

            self.backButton.setEnabled(True)
            self.nextButton.setEnabled(True)
        else:
            self.playPauseButton.setText('Play')
            self.backButton.setEnabled(False)
            self.nextButton.setEnabled(False)


    def loadImage(self, imageFile):
        image = QImage(imageFile)
        self.mainPicturePixmap.convertFromImage(image)

        print('PicturePixmap.size: '
                + str(self.mainPicturePixmap.width())
                + ' x '
                + str(self.mainPicturePixmap.height()))

        print('PictureLabel.size: '
                + str(self.mainPictureWidget.width())
                + ' x '
                + str(self.mainPictureWidget.height()))

        self.mainPictureWidget.setPixmap(self.mainPicturePixmap)
        self.titleLabel.setText(imageFile)

    def backButtonAction(self):
        imageCount = len(self.imageList)
        if imageCount <= 0 or self.playState == False:
            return

        nextImage = self.imageIndex - 1
        nextImage %= imageCount

        if nextImage != self.imageIndex:
            self.loadImage(self.imageList[nextImage])
            self.imageIndex = nextImage


    def nextButtonAction(self):
        imageCount = len(self.imageList)
        if imageCount <= 0 or self.playState == False:
            return

        nextImage = self.imageIndex + 1
        nextImage %= imageCount

        if nextImage != self.imageIndex:
            self.loadImage(self.imageList[nextImage])
            self.imageIndex = nextImage


    def initMenuBar(self):
        # Initialize menu bar
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)

        # Initialize File menu components
        importAction = QAction('Import', self)
        importAction.triggered.connect(self.importFile)
        importAction.setStatusTip('Import File')
        importAction.setShortcut('Ctrl+O')

        importDirAction = QAction('Import Dir', self)
        importDirAction.triggered.connect(self.importDir)
        importDirAction.setStatusTip('Import Directory')

        quitAction = QAction('Quit', self)
        quitAction.triggered.connect(self.close)
        quitAction.setStatusTip('Quit Application')
        quitAction.setShortcut('Ctrl+Q')

        # Build file menu
        fileMenu = menubar.addMenu('File')
        fileMenu.addAction(importAction)
        fileMenu.addAction(importDirAction)
        fileMenu.addSeparator()
        fileMenu.addAction(quitAction)

    def importDir(self):
        dirName = QFileDialog.getExistingDirectory(self, 'Open Directory', QDir.currentPath())

        print('dirName: ' + dirName)

        self.imageList.appendDirectory(dirName)

        print(self.imageList)


    def importFile(self):
        imageFile, _ = QFileDialog.getOpenFileName(
            self, 'Open File', QDir.currentPath())

        self.imageList.addImage(imageFile)





if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWin = FuzzyDoodlePlayer()
    mainWin.show()
    sys.exit(app.exec_())
