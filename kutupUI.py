import sys
from PyQt5 import QtWidgets, uic

from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget, QPushButton, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QImage
from PyQt5.QtCore import pyqtSignal, QObject
import kutuphane as ktp
from uiConnection import uiCon
class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('kutup.ui', self)
        
        # self.uiProps = uiCon(self)
        

        self.show()
        
        

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()