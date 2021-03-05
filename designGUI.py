import sys

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtGui import QImage, QPixmap, QTransform
from PyQt5.QtWidgets import QApplication, QFileDialog, QLabel, QWidget, QPushButton, QDesktopWidget

class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('GUI')
        self.resize(440, 680)
        self.initUI()
    
    
    def initUI(self):
        self.impButton = QPushButton('Import', self)
        self.impButton.resize(160, 40)
        self.impButton.move(40, 440)

        self.label = QLabel(self)
        self.setLabel('anh.jpg')

        self.impButton.clicked.connect(self.clickImp)
        
        self.expButton = QPushButton('Export', self)
        self.expButton.resize(160, 40)
        self.expButton.move(240, 440)
        self.expButton.clicked.connect(self.clickExp)

        self.rlButton = QPushButton('Rotate Left', self)
        self.rlButton.resize(160, 40)
        self.rlButton.move(40, 520)
        self.rlButton.clicked.connect(self.clickRL)

        self.rrButton = QPushButton('Rotate Right', self)
        self.rrButton.resize(160, 40)
        self.rrButton.move(240, 520)
        self.rrButton.clicked.connect(self.clickRR)

        self.graButton = QPushButton('Grayscale', self)
        self.graButton.resize(160, 40)
        self.graButton.move(40, 600)
        self.graButton.clicked.connect(self.clickGrayscale)

        self.undoButton = QPushButton('Undo', self)
        self.undoButton.resize(160, 40)
        self.undoButton.move(240, 600)
        
        self.center()
        

    # move the frame to center of screen
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def setLabel(self, imgPath):
        self.pm = QPixmap(imgPath).scaled(360, 360, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(self.pm)
        self.label.move(40, 40)

    def clickImp(self):
        options = QFileDialog.Options()
        fName = QFileDialog.getOpenFileName(self, "Open a image","", "Image files (*.jpg *.png);;All File(*)", options=options)
        imgPath = fName[0]
        if imgPath:
            self.setLabel(imgPath)

    def clickExp(self):
        options = QFileDialog.Options()
        fName = QFileDialog.getSaveFileName(self, "Open a image","", "Image files (*.jpg)", options=options)
        imgPath = fName[0]
        if imgPath:
            self.pm.save(imgPath)

    def clickRL(self):
        tf = QTransform().rotate(-90)
        self.pm = self.pm.transformed(tf, QtCore.Qt.SmoothTransformation)
        self.label.setPixmap(self.pm)

    def clickRR(self):
        tf = QTransform().rotate(90)
        self.pm = self.pm.transformed(tf, QtCore.Qt.SmoothTransformation)
        self.label.setPixmap(self.pm)

    def clickGrayscale(self):
        img = QPixmap.toImage(self.pm)
        grayscale = img.convertToFormat(QImage.Format_Grayscale8)
        self.pm = QPixmap.fromImage(grayscale)
        self.label.setPixmap(self.pm)

def main():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()