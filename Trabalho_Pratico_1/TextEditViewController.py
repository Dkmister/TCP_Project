import easygui
import Strings

class TextEditViewController:
    
    def __init__(self):
        self.currentFile = ""
        self.displayView()
        
    def displayView(self):
        easygui.codebox("msg","Title","text from file") 