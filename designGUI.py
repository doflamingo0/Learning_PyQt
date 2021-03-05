import sys

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QFileDialog, QLabel, QMainWindow, QWidget, QPushButton, QDesktopWidget

class MyWindow(QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.centralWidget = QWidget(self)
        self.setWindowTitle('GUI')
        self.resize(440, 680)
        self.initUI()
    
    
    def initUI(self):
        self.impButton = QPushButton('Import', self)
        self.impButton.resize(160, 40)
        self.impButton.move(40, 440)

        self.label = QLabel(self)
        self.pixmap = QPixmap()
        self.impButton.clicked.connect(self.clickImp)

        self.expButton = QPushButton('Export', self)
        self.expButton.resize(160, 40)
        self.expButton.move(240, 440)

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


    def clickImp(self):
        options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog
        fName, _ = QFileDialog.getOpenFileName(self, "Open a image", "", "All File(*);;Image files (*.jpg *.png)", options=options)
        if fName:
            self.pixmap = QPixmap(fName)
            self.pixmap = self.pixmap.scaled(360, 360, QtCore.Qt.KeepAspectRatio)
            self.label.setPixmap(self.pixmap)
            self.label.move(40, 40)

            # print(self.pixmap.size())


def main():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()