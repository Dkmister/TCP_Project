import easygui
import Strings
from TextEditViewController import * 

class MainViewController:
    
    def __init__(self):
        self.currentFile = ""
        self.textEditView = None
        self.choices = [Strings.NEW_FILE, Strings.OPEN_FILE, Strings.EDIT_FILE, Strings.PLAY_AUDIO, Strings.EXPORT_AUDIO]
        self.choicesActions = [self.newFile]
        self.displayView()
        
    def displayView(self):
        msg = "Arquivo atual: " + self.currentFile + "\n "
        choice = easygui.indexbox("msg",Strings.SOFTWARE_TITLE,self.choices)
        self.choicesActions[choice]()
        
    def newFile(self):
        self.textEditView = TextEditViewController()


m = MainViewController()
while True:
    m.displayView()