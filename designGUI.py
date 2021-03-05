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
        self.listStatus = []
        self.x = 0
        self.y = 0
        self.initUI()
        

    def initUI(self):
        # import button
        self.impButton = QPushButton('Import', self)
        self.impButton.resize(160, 40)
        self.impButton.move(40, 440)
        self.label = QLabel(self)
        self.setLabel('anh.jpg')
        self.impButton.clicked.connect(self.clickImp)
        
        # export button
        self.expButton = QPushButton('Export', self)
        self.expButton.resize(160, 40)
        self.expButton.move(240, 440)
        self.expButton.clicked.connect(self.clickExp)

        # rotate left button
        self.rlButton = QPushButton('Rotate Left', self)
        self.rlButton.resize(160, 40)
        self.rlButton.move(40, 520)
        self.rlButton.clicked.connect(self.clickRL)

        # rotate right button
        self.rrButton = QPushButton('Rotate Right', self)
        self.rrButton.resize(160, 40)
        self.rrButton.move(240, 520)
        self.rrButton.clicked.connect(self.clickRR)

        # grayscale button
        self.graButton = QPushButton('Grayscale', self)
        self.graButton.resize(160, 40)
        self.graButton.move(40, 600)
        self.graButton.clicked.connect(self.clickGrayscale)

        # undo button
        self.undoButton = QPushButton('Undo', self)
        self.undoButton.resize(160, 40)
        self.undoButton.move(240, 600)
        self.undoButton.clicked.connect(self.clickUndo)

        self.center()
        

    # update position
    def update(self):
        self.x = int((440 - self.image.width())/2)
        self.y = int((440 - self.image.height())/2)
        self.label.move(self.x, self.y)


    # move the frame to center of screen
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    # set image of label
    def setLabel(self, imgPath):
        self.listStatus.clear()
        self.image = QPixmap(imgPath).scaled(360, 360, QtCore.Qt.KeepAspectRatio)
        self.listStatus.append(self.image)
        self.label.setPixmap(self.image)
        self.update()


    # click import button
    def clickImp(self):
        options = QFileDialog.Options()
        fName = QFileDialog.getOpenFileName(self, "Open a image","", "Image files (*.jpg *.png);;All File(*)", options=options)
        imgPath = fName[0]
        if imgPath:
            self.setLabel(imgPath)


    # click export button
    def clickExp(self):
        options = QFileDialog.Options()
        fName = QFileDialog.getSaveFileName(self, "Open a image","", "Image files (*.jpg)", options=options)
        imgPath = fName[0]
        if imgPath:
            self.image.save(imgPath)


    # click rotate left button
    def clickRL(self):
        tf = QTransform().rotate(-90)
        self.image = self.image.transformed(tf, QtCore.Qt.SmoothTransformation)
        self.listStatus.append(self.image)
        self.label.setPixmap(self.image)
        self.update()


    # click rotate right button
    def clickRR(self):
        tf = QTransform().rotate(90)
        self.image = self.image.transformed(tf, QtCore.Qt.SmoothTransformation)
        self.listStatus.append(self.image)
        self.label.setPixmap(self.image)
        self.update()


    # click grayscale button
    def clickGrayscale(self):
        img = QPixmap.toImage(self.image)
        grayscale = img.convertToFormat(QImage.Format_Grayscale8)
        self.image = QPixmap.fromImage(grayscale)
        self.listStatus.append(self.image)
        self.label.setPixmap(self.image)


    # click undo button
    def clickUndo(self):
        length = len(self.listStatus)
        if length > 1:
            self.listStatus.pop()
            self.image = self.listStatus[length-2]
            self.label.setPixmap(self.image)
            self.update()


def main():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()