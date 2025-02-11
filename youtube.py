# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\projeto youtube.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from mhyt import yt_download
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(686, 413)
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.download_bt = QtWidgets.QPushButton(self.centralwidget)
        self.download_bt.setGeometry(QtCore.QRect(480, 280, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.download_bt.setFont(font)
        self.download_bt.setObjectName("download_bt")
        self.link_label = QtWidgets.QLabel(self.centralwidget)
        self.link_label.setGeometry(QtCore.QRect(80, 180, 55, 23))
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.link_label.setFont(font)
        self.link_label.setObjectName("link_label")
        self.titulo_label = QtWidgets.QLabel(self.centralwidget)
        self.titulo_label.setGeometry(QtCore.QRect(80, 220, 87, 23))
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.titulo_label.setFont(font)
        self.titulo_label.setObjectName("titulo_label")
        self.titulo_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.titulo_txt.setGeometry(QtCore.QRect(180, 220, 411, 20))
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.titulo_txt.setFont(font)
        self.titulo_txt.setObjectName("titulo_txt")
        self.link_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.link_txt.setGeometry(QtCore.QRect(180, 180, 411, 20))
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.link_txt.setFont(font)
        self.link_txt.setText("")
        self.link_txt.setObjectName("link_txt")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(180, 260, 65, 54))
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.splitter.setFont(font)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.type_mp3 = QtWidgets.QRadioButton(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.type_mp3.setFont(font)
        self.type_mp3.setChecked(True)
        self.type_mp3.setObjectName("type_mp3")
        self.type_mp4 = QtWidgets.QRadioButton(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.type_mp4.setFont(font)
        self.type_mp4.setChecked(False)
        self.type_mp4.setObjectName("type_mp4")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setGeometry(QtCore.QRect(130, -20, 395, 200))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.label_4 = QtWidgets.QLabel(self.splitter_2)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 686, 29))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

# Botão de Download
        self.download_bt.clicked.connect(self.download)

    def download(self):
        if self.type_mp4.isChecked() == True:
            url = self.link_txt.text()
            titulo = self.titulo_txt.text()
            titulo_mp4 = titulo + '.mp4'
            yt_download(url,titulo_mp4)

        elif self.type_mp3.isChecked() == True:
            try:
                url = self.link_txt.text()
                titulo = self.titulo_txt.text()
                titulo_mp3= titulo + '.mp3'
                yt_download(url,titulo_mp3,ismusic=True,codec='mp3')
            except:
                pass


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.download_bt.setText(_translate("MainWindow", "Download"))
        self.link_label.setText(_translate("MainWindow", "LINK:"))
        self.titulo_label.setText(_translate("MainWindow", "TITULO:"))
        self.type_mp3.setText(_translate("MainWindow", "MP3"))
        self.type_mp4.setText(_translate("MainWindow", "MP4"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/Youtube/24709-7-youtube-transparent-image-thumb.png\"/></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "DOWNLOAD"))

# imagem do yotube
import logo

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
