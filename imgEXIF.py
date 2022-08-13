from exif import Image
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import tkinter as tk
from tkinter.filedialog import askopenfilename
import sys
import json

def openfile():
    tk.Tk().withdraw()
    fn = askopenfilename()
    return fn

def get_exif(img):
    exif_dict = {}
    if img != '':
        with open(img, 'rb') as f:
            f = Image(f)

        if f.has_exif:
            for i in f.list_all():
                try:
                    # exif_dict[i] = eval(f'f.{i}')
                    exif_dict[i] = str(f[i])
                except:
                    exif_dict[i] = 'ERROR'

    result = json.dumps(exif_dict, sort_keys=True, indent=4)
    return result

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.img = ''
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(677, 507)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 50, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(60, 140, 301, 281))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(170, 50, 441, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBar.setGeometry(QtCore.QRect(360, 140, 21, 281))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 110, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(480, 260, 47, 13))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 677, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def get_img(self):
        self.img = r"{}".format(openfile())
        self.textEdit_2.setText(self.img)
        data = get_exif(self.img)
        self.textEdit.setText(data)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle("EXIF Data Viewer")
        self.label.setText(_translate("MainWindow", "Summary"))
        # self.label_2.setText(_translate("MainWindow", "img"))
        pixmap = QPixmap(self.img)
        self.label_2.setPixmap(pixmap.scaled(200, 200))
        # MainWindow.setCentralWidget(self.label_2)
        self.pushButton.setText(_translate("MainWindow", "Open..."))
        self.pushButton.clicked.connect(lambda: self.get_img())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
