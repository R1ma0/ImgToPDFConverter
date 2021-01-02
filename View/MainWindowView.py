"""
"""



from PyQt5 import QtWidgets
from View.MainWindowUI import Ui_MainWindow



class MainWindowView(QtWidgets.QMainWindow):
    """
    docstring
    """
    def __init__(self, controller, model):
        """
        """
        super(MainWindowView, self).__init__()
        self.controller = controller
        self.model = model

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
