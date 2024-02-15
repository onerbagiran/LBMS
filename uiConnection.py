from PyQt5.QtWidgets import QMainWindow, QApplication, QSplashScreen
from PyQt5.QtCore import QCoreApplication, Qt, QSettings, QObject, QThread, pyqtSignal, QPointF
from PyQt5.QtGui import QPixmap


class uiCon(object):
    def __init__(self,ui):
        self.ui = ui
      


        ui.pbKitapEkle.clicked.connect(self.fnKitapEkle)
        ui.pbCikis.clicked.connect(self.fnCikis)

        
    def fnCikis(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.buttons)
    def fnKitapEkle(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.kitapekle)
        # ui.pbLive.clicked.connect(self.fnLive)
        # ui.pbSettings.clicked.connect(self.fnSettings)
        # ui.pbInfo.clicked.connect(self.fnInfo)



        # self.ui.widgetPopup.raise_()
        # self.ui.stackedWidgetPopup.setCurrentWidget(self.ui.pgSaveImageName)