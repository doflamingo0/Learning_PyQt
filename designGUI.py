import sys
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDesktopWidget
from PyQt5.QtGui import QTextFrame

class UI(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
    
    
    def initUI(self):

        impButton = QPushButton('Import', self)
        expButton = QPushButton('Export', self)
        rlButton = QPushButton('Rotate Left', self)
        rrButton = QPushButton('Rotate Right', self)
        graButton = QPushButton('Grayscale', self)
        undoButton = QPushButton('Undo', self)

        impButton.resize(160, 40)
        expButton.resize(160, 40)
        rlButton.resize(160, 40)
        rrButton.resize(160, 40)
        graButton.resize(160, 40)
        undoButton.resize(160, 40)

        impButton.move(40, 440)
        expButton.move(240, 440)
        rlButton.move(40, 520)
        rrButton.move(240, 520)
        graButton.move(40, 600)
        undoButton.move(240, 600)

        self.resize(440, 680)
        self.center()
        self.setWindowTitle('GUI')
        self.show()

    
    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())



def main():

    app = QApplication(sys.argv)
    ex = UI()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()    

        




