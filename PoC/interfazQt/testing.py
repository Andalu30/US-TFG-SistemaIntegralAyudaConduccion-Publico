# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(0, 0, 401, 401))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("../../../../Imágenes/avatarBabel.jpg"))
        self.photo.setScaledContents(False)
        self.photo.setObjectName("photo")

        self.babelButton = QtWidgets.QPushButton(self.centralwidget)
        self.babelButton.setGeometry(QtCore.QRect(470, 70, 241, 91))
        self.babelButton.setObjectName("babelButton")
        self.normalButton = QtWidgets.QPushButton(self.centralwidget)
        self.normalButton.setGeometry(QtCore.QRect(470, 190, 241, 91))
        self.normalButton.setObjectName("normalButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



        self.babelButton.clicked.connect(self.showbabel)
        self.normalButton.clicked.connect(self.showNormal)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.babelButton.setText(_translate("MainWindow", "BABEL"))
        self.normalButton.setText(_translate("MainWindow", "NORMAL"))


    def showbabel(self):
        self.photo.setPixmap(QtGui.QPixmap("../../../../Imágenes/avatarBabel.jpg"))

    def showNormal(self):
        self.photo.setPixmap(QtGui.QPixmap("../../../../Imágenes/avatar.jpg"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
