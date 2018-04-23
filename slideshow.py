import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import (QMainWindow, QFileDialog, QLabel, QGridLayout,
                             QWidget, QAction)
from PyQt5.QtCore import QDir, QSize
from PyQt5.QtGui import QPixmap, QImage


class HelloWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.initWindow()
        self.initMenuBar()
        self.initBody()

        # Inform user that we"re ready for use
        self.statusBar().showMessage("Ready!")

    def initWindow(self):
        self.setMinimumSize(QSize(640, 480))
        self.setWindowTitle("Hello World")

    def initBody(self):
        # Setup central grid layout
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        gridLayout = QGridLayout(self)
        centralWidget.setLayout(gridLayout)

        # Add labels to layout
        titleLabel = QLabel("Hello World from PyQt", self)
        titleLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.mainPictureLabel = QLabel(self)
        self.mainPictureLabel.scaleFactor = 1.0
        self.mainPictureLabel.setAlignment(QtCore.Qt.AlignCenter)

        gridLayout.addWidget(titleLabel, 0, 0)
        gridLayout.addWidget(self.mainPictureLabel, 1, 0)

    def initMenuBar(self):
        # Initialize menu bar
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)

        # Initialize File menu

        openAction = QAction("Open", self)
        openAction.triggered.connect(self.openFile)
        openAction.setStatusTip("Open File")

        quitAction = QAction("Quit", self)
        quitAction.triggered.connect(self.close)
        quitAction.setStatusTip("Quit Application")
        quitAction.setShortcut("Ctrl+Q")

        # Build file menu
        fileMenu = menubar.addMenu("File")
        fileMenu.addAction(openAction)
        fileMenu.addSeparator()
        fileMenu.addAction(quitAction)

    def openFile(self):
        self.imageFilename, _ = QFileDialog.getOpenFileName(
            self, "Open File", QDir.currentPath())

        image = QImage(self.imageFilename)
        self.mainPictureLabel.setPixmap(QPixmap.fromImage(image))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = HelloWindow()
    mainWin.show()
    sys.exit(app.exec_())
