""" This file contains the view class of the main window """



from PyQt5 import QtWidgets
from View.MainWindowUI import Ui_MainWindow



class MainWindowView(QtWidgets.QMainWindow):
    """ Main window view methods """
    def __init__(self, controller):
        """ UI & Controller initizization """
        super(MainWindowView, self).__init__()
        self.controller = controller            # Controller init

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionOpen_Image.triggered.connect(self.controller.OpenImage)

