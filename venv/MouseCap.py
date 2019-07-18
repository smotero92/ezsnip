import sys
from PyQt5.QtWidgets import (QApplication, QLabel, QWidget)

class MouseTracker(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setMouseTracking(True)

    def initUI(self):
        self.setGeometry(300,300,1980,1000)
        self.setWindowTitle('MouseTracker')
        self.label = QLabel(self)
        self.label.resize(200,40)
        self.show()

    def mouseMoveEvent(self, event):
        self.label.setText('Mouse Coordinates: ( %d : %d )' % (event.x(), event.y()))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MouseTracker()
    sys.exit(app.exec_())