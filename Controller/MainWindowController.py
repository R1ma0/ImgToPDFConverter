""" This file contains the controller class of the main window """



from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap
from View.MainWindowView import MainWindowView



class MainWindowController(object):
    """ Main window controller methods """
    def __init__(self, model):
        """ Class initialization """
        self.model = model                              # Model init
        self.view = MainWindowView(self)                # View init
        self.view.show()                                # View showing

    def OpenImage(self):
        """ Open image from disk """
        fileName = QFileDialog.getOpenFileName(self.view, 'Open Image', '/home')[0]
        pixmap = QPixmap(fileName)   
        frame = self.view.ui.frame
        self.view.ui.imageToPdf.setGeometry(0, 0, frame.frameGeometry().width(), frame.frameGeometry().height())       
        self.view.ui.imageToPdf.setPixmap(pixmap)  