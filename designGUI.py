import sys

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
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

        self.rrButton = QPushButton('Rotate Right', self)
        self.rrButton.resize(160, 40)
        self.rrButton.move(240, 520)

        self.graButton = QPushButton('Grayscale', self)
        self.graButton.resize(160, 40)
        self.graButton.move(40, 600)

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
        self.pm = QPixmap(imgPath)
        self.label.setPixmap(self.pm.scaled(360, 360, QtCore.Qt.KeepAspectRatio))
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

def main():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()