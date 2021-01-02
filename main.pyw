"""
"""



import sys
from PyQt5 import QtWidgets
from Controller.MainWindowController import MainWindowController
from Model.MainWindowModel import MainWindowModel



def main():
    app = QtWidgets.QApplication([])
    model = MainWindowModel()
    controller = MainWindowController(model)
    app.exec_()

if __name__ == '__main__':
    sys.exit(main())