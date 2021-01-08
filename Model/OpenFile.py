""" """



from PyQt5.QtWidgets import QFileDialog



class UploadFileNames(object):
    """
    docstring
    """
    def __init__(self, view):
        self.view = view

    def Load(self):
        return QFileDialog.getOpenFileNames(self.view, 'Open Image', '/')[0]