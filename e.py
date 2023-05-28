from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys


def Window():
    app= QApplication(sys.argv)
    win=QMainWindow()
    win.setGeometry(20,20,30,30)
    win.setWindowTitle("TEcH")
    
    win.show()
    sys.exit(app.exec_())
   
Window()