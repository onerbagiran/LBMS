import sys
from PyQt5 import QtWidgets, uic

from PyQt5.QtWidgets import QApplication, QLabel, QTableWidgetItem, QMainWindow, QVBoxLayout, QWidget, QPushButton, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QImage
from PyQt5.QtCore import pyqtSignal, QObject
import kutuphane as ktp
from uiConnection import uiCon
class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('kutup.ui', self)

        self.uiProps = uiCon(self)
        self.sonSatir = 0 
        self.pbKitapKaydet.clicked.connect(self.fnKitapKaydet)
        self.pbKitapSil.clicked.connect(self.fnKitapSil)

        self.tablo.setColumnCount(4)
        self.tablo.setRowCount(1000)
        self.fnTabloDoldurma()
        self.show()
        
    def fnTabloDoldurma(self):
        #bu kısımda daha önce kaydedilmiş kitaplar init kısmında tabloya ekleniyor
        self.tablo.clear()
        try:
            with open("books.txt", "r") as dosya:
                print("hello")
                satirlar = dosya.readlines()
                print()
                for satir_index, satir in enumerate(satirlar):
                    veriler = satir.strip().split(",")
                    for sutun_index, veri in enumerate(veriler):
                        self.tablo.setItem(satir_index, sutun_index, QTableWidgetItem(str(veri)))
                        print(satir_index)
                        self.sonSatir = satir_index 
                        
                        
        except FileNotFoundError:
            print("Dosya bulunamadı.")
    def fnKitapKaydet(self):
        self.strKitapAdi     = self.textKitapAdi.toPlainText()
        self.strKitapYazari  = self.textKitapYazari.toPlainText()
        self.strCikisTarihi  = self.textCikisTarihi.toPlainText()
        self.strSayfaSayisi  = self.textSayfaSayisi.toPlainText()
        self.tablo.setItem(self.sonSatir+1, 0, QTableWidgetItem(self.strKitapAdi))
        self.tablo.setItem(self.sonSatir+1, 1, QTableWidgetItem(self.strKitapYazari))
        self.tablo.setItem(self.sonSatir+1, 2, QTableWidgetItem(self.strCikisTarihi))
        self.tablo.setItem(self.sonSatir+1, 3, QTableWidgetItem(self.strSayfaSayisi))
        self.sonSatir = self.sonSatir + 1 
        Kitabin_kunyesi=f"{str(self.strKitapAdi)},{self.strKitapYazari},{self.strCikisTarihi},{self.strSayfaSayisi}\n"
        self.file=open("books.txt","a+")

        self.file.write(Kitabin_kunyesi)
        self.file.seek(0)
        # self.file.close()
        self.fnTextEditTemizleme()
    def fnTextEditTemizleme(self):
        self.textKitapAdi.clear()
        self.textKitapYazari.clear()
        self.textCikisTarihi.clear()
        self.textSayfaSayisi.clear()
    def fnTextSilmeTemizleme(self):
        self.textKitapAdiSilme.clear()
    def fnKitapSil(self):
        silinecek_kitap=self.textKitapAdiSilme.toPlainText()
        dosya_yolu = "books.txt"
        try:
            gecici_dosya_yolu = dosya_yolu + ".gecici"
            with open(dosya_yolu, "r") as dosya, open(gecici_dosya_yolu, "w") as gecici_dosya:
                for satir in dosya:
                    parcalar = satir.strip().split(",")
                    if parcalar[0] != silinecek_kitap:
                        gecici_dosya.write(satir)

            import shutil
            shutil.move(gecici_dosya_yolu, dosya_yolu)

            print("Veriler başarıyla silindi.")
            self.fnTabloDoldurma()

        except Exception as e:
            print("Veri silinirken bir hata oluştu:", str(e))      

        
        print("burada")

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()