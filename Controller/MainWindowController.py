"""

"""



from View.MainWindowView import MainWindowView



class MainWindowController(object):
    """
    docstring
    """
    def __init__(self, model):
        """
        """
        self.model = model
        self.view = MainWindowView(self, self.model)
        self.view.show()