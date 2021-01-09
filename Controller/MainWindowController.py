""" This file contains the controller class of the main window """



from View.MainWindowView import MainWindowView



class MainWindowController(object):
    """ Main window controller methods """
    def __init__(self, model):
        """ Class initialization """
        self.model = model                              # Model init
        self.view = MainWindowView(self)                # View init
        self.view.show()                                # View showing
        self.fileNames = []                             # Uploaded file names

    def openFileNames(self):
        """ Upload file names from storage """
        self.fileNames = self.model.uploadFileNames(self.view)
        self.showOpenFileNames(self.fileNames)

    def showOpenFileNames(self, fileNames):
        """ Display file names in QListWidget """
        self.view.ui.listWidget.addItems(fileNames)

    def exportToPDF(self):
        """ Export a list of files to PDF format """
        if self.fileNames:
            result = self.model.savePDF(self.view, self.fileNames)
            self.view.ui.statusbar.showMessage(result)
        else:
            result = "Select files to export"
            self.view.ui.statusbar.showMessage(result)

    def clearFileNames(self):
        """  """
        if self.fileNames:
            self.fileNames.clear()
            self.view.ui.listWidget.clear()
            message = "File list cleared"
            self.view.ui.statusbar.showMessage(message)