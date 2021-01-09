""" This file contains the model class of the main window """



from PyQt5.QtWidgets import QFileDialog
from PIL import Image



class MainWindowModel(object):
    """ Main window model methods """
    def __init__(self):
        pass

    def uploadFileNames(self, view):
        """ Upload file names from storage """
        parent = view
        title = 'Open Image'
        path = '/'
        filter = 'Images (*.png *jpg *.jpeg)'
        return QFileDialog.getOpenFileNames(parent, title, path, filter)[0]

    def savePDF(self, view, fileNames):
        """ Saving PDF file """
        # Path To Save
        parent = view
        title = 'Path To Save'
        path = '/'
        filter = 'PDF (*.pdf)'
        pathToSave = QFileDialog.getSaveFileName(parent, title, path, filter)[0]

        if not pathToSave:
            return "Save path was not specified"

        # Creating PDF File
        imageList = []

        for path in fileNames:
            image = Image.open(path)
            imageList.append(image.convert('RGB'))

        imageList[0].save(pathToSave, save_all=True, append_images=imageList[1:])

        return "Saving was successful (" + pathToSave + ")"