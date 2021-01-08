""" This file contains the controller class of the main window """



from Model.OpenFile import UploadFileNames
from View.MainWindowView import MainWindowView



class MainWindowController(object):
    """ Main window controller methods """
    def __init__(self, model):
        """ Class initialization """
        self.model = model                              # Model init
        self.view = MainWindowView(self)                # View init
        self.view.show()                                # View showing
        self.ufn = UploadFileNames(self.view)
        self.fileNames = []

    def OpenFileNames(self):
        """ Uploadd file names from disk """
        self.fileNames = self.ufn.Load()
        self.ShowOpenFileNames(self.fileNames)

    def ShowOpenFileNames(self, fileNames):
        self.view.ui.listWidget.addItems(fileNames)
        