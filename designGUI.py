import sys
import cv2 as cv
from PyQt5 import QtCore
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QFileDialog, QLabel, QWidget, QPushButton, QDesktopWidget

class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('GUI')
        self.resize(440, 680)
        self.listStatus = []
        self.mark = 0   # = 1 if gray image, = 0 if not gray image
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
        

    # update position and label of rgb image
    def updateRGB(self):
        temp = QImage(self.image.data, self.image.shape[1], self.image.shape[0], 3*self.image.shape[1], QImage.Format_RGB888).rgbSwapped()
        temp = QPixmap.fromImage(temp).scaled(360, 360, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(temp)

        self.x = int((440 - temp.width())/2)
        self.y = int((440 - temp.height())/2)
        self.label.move(self.x, self.y)


    # update position and label of gray image
    def updateGray(self):
        temp = QImage(self.image.data, self.image.shape[1], self.image.shape[0], self.image.shape[1], QImage.Format_Indexed8)
        temp = QPixmap.fromImage(temp).scaled(360, 360, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(temp)

        self.x = int((440 - temp.width())/2)
        self.y = int((440 - temp.height())/2)
        self.label.move(self.x, self.y)


    # move the frame to center of screen
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    # set image of label
    def setLabel(self, imgPath):
        self.image = cv.imread(imgPath)
        self.mark = 0
        self.listStatus.clear()
        self.listStatus.append([self.image, self.mark])
        self.updateRGB()


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
            cv.imwrite(imgPath, self.image)


    # click rotate left button
    def clickRL(self):
        self.image = cv.rotate(self.image, cv.ROTATE_90_COUNTERCLOCKWISE)
        self.listStatus.append([self.image, self.mark])
        if self.mark == 0:
            self.updateRGB()
        else:
            self.updateGray()


    # click rotate right button
    def clickRR(self):
        self.image = cv.rotate(self.image, cv.ROTATE_90_CLOCKWISE)
        self.listStatus.append([self.image, self.mark])
        if self.mark == 0:
            self.updateRGB()
        else:
            self.updateGray()


    # click grayscale button
    def clickGrayscale(self):
        if self.mark == 0:
            self.mark = 1
            self.image = cv.cvtColor(self.image, cv.COLOR_BGR2GRAY)
            self.listStatus.append([self.image, self.mark])
            self.updateGray()


    # click undo button
    def clickUndo(self):
        length = len(self.listStatus)
        if length > 1:
            self.listStatus.pop()
            self.image, self.mark = self.listStatus[length-2]
            if self.mark == 1:
                self.updateGray()
            else:
                self.updateRGB()


def main():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()