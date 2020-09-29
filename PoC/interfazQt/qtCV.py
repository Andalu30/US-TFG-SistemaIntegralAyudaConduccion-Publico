import sys
import cv2
import numpy as np

from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel()
        self.initUI()
        self.actualizaImg(None)

    def initUI(self):
        self.label.setText('OpenCV Image')
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet( 'border: gray; border-style:solid; border-width: 1px;')

        self.resize(540, 574)
        self.setWindowTitle('Testeo OpenCV + pyQt5')

    def actualizaImg(self, cvImg):
        if cvImg is None:
            pass
        else:
            print('actualiza')
            height, width, channel = cvImg.shape
            bytesPerLine = 3 * width
            qImg = QImage(cvImg.data, width, height, bytesPerLine, QImage.Format_RGB888)
            print(qImg)

            self.label.setPixmap(QPixmap.fromImage(qImg))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Example()

    frame = cv2.imread('/home/andalu30/Imágenes/avatar.jpg')
    win.actualizaImg(frame)

    win.show()

    sys.exit(app.exec_())
