from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import (QMainWindow, QLabel, QGridLayout, QAction,
                             QPushButton, QSizePolicy, QWidget, QHBoxLayout)
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap
from ImageScaleWidget import ImageScaleWidget


class FuzzyDoodleUi(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        self.statusBar = self.statusBar()

        # Initialize GUI
        self.initWindow()
        self.initMenuBar()
        self.initBody()

        # Inform user that we're ready for use
        self.statusBar.showMessage('Ready!')

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

        mainGridLayout = QGridLayout(self)
        centralWidget.setLayout(mainGridLayout)

        self.initPictureFrame()
        self.initBodyButtons()

        # Add widgets to layout
        mainGridLayout.addWidget(self.mainPictureWidget, 0, 1)
        mainGridLayout.addWidget(self.titleLabel, 1, 1)
        mainGridLayout.addLayout(self.buttonLayout, 2, 1)

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
        self.backButton.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.backButton.setEnabled(False)

        # Create pause/play button
        self.playPauseButton = QPushButton('Play', self)
        self.playPauseButton.setToolTip('Start/continue practice session')
        self.playPauseButton.setSizePolicy(QSizePolicy.Minimum,
                                           QSizePolicy.Fixed)
        self.playPauseButton.setEnabled(False)

        # Create next button
        self.nextButton = QPushButton('Next', self)
        self.nextButton.setToolTip('Go to next image')
        self.nextButton.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.nextButton.setEnabled(False)

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
        self.importAction = QAction('Import', self)
        self.importAction.setStatusTip('Import File')
        self.importAction.setShortcut('Ctrl+O')

        self.importDirAction = QAction('Import Dir', self)
        self.importDirAction.setStatusTip('Import Directory')

        self.quitAction = QAction('Quit', self)
        self.quitAction.triggered.connect(self.close)
        self.quitAction.setStatusTip('Quit Application')
        self.quitAction.setShortcut('Ctrl+Q')

        # Build file menu
        self.fileMenu = menubar.addMenu('File')
        self.fileMenu.addAction(self.importAction)
        self.fileMenu.addAction(self.importDirAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.quitAction)
