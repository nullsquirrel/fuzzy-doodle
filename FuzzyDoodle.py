import sys
from PyQt5 import QtWidgets
import FuzzyDoodlePlayer

app = QtWidgets.QApplication(sys.argv)
mainWin = FuzzyDoodlePlayer()
mainWin.ui.show()
sys.exit(app.exec_())
