import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import (QMainWindow, QFileDialog, QLabel, QGridLayout,
                             QWidget, QAction, QPushButton, QHBoxLayout,
                             QSizePolicy)
from PyQt5.QtCore import QDir, QSize
from PyQt5.QtGui import QPixmap, QImage
from imageScaleWidget import ImageScaleWidget


class FuzzyDoodlePlayer(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        # Capture screen geometry prior to GUI initialization
        self.screenGeometry = QtWidgets.QApplication.desktop().screenGeometry()

        # Initialize GUI
        self.initWindow()
        self.initMenuBar()
        self.initBody()

        # Inform user that we're ready for use
        self.statusBar().showMessage('Ready!')

    def initWindow(self):
        requestedSize = QSize(self.screenGeometry.width()*2/3,
                                self.screenGeometry.height()*2/3)
        self.setMinimumSize(320, 240)
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
        self.backButton.clicked.connect(self.nextButtonAction)
        self.backButton.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        # Create pause/play button
        self.playPauseButton = QPushButton('Play', self)
        self.playPauseButton.setToolTip('Start/continue practice session')
        self.playPauseButton.clicked.connect(self.nextButtonAction)
        self.playPauseButton.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        # Create next button
        self.nextButton = QPushButton('Next', self)
        self.nextButton.setToolTip('Go to next image')
        self.nextButton.clicked.connect(self.nextButtonAction)
        self.nextButton.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

        # Create button widget
        self.buttonLayout = QHBoxLayout(self)
        self.buttonLayout.addWidget(self.backButton)
        self.buttonLayout.addWidget(self.playPauseButton)
        self.buttonLayout.addWidget(self.nextButton)


    def initMenuBar(self):
        # Initialize menu bar
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)

        # Initialize File menu components
        openAction = QAction('Open', self)
        openAction.triggered.connect(self.openFile)
        openAction.setStatusTip('Open File')
        openAction.setShortcut('Ctrl+O')

        quitAction = QAction('Quit', self)
        quitAction.triggered.connect(self.close)
        quitAction.setStatusTip('Quit Application')
        quitAction.setShortcut('Ctrl+Q')

        # Build file menu
        fileMenu = menubar.addMenu('File')
        fileMenu.addAction(openAction)
        fileMenu.addSeparator()
        fileMenu.addAction(quitAction)


    def openFile(self):
        self.imageFilename, _ = QFileDialog.getOpenFileName(
            self, 'Open File', QDir.currentPath())

        image = QImage(self.imageFilename)
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
        self.titleLabel.setText(self.imageFilename)


    def nextButtonAction(self):
        self.mainPictureWidget.clear()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWin = FuzzyDoodlePlayer()
    mainWin.show()
    sys.exit(app.exec_())
