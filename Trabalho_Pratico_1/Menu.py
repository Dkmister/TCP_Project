import easygui
import Strings
# Must have a import from the others classes to interact between them

# easygui allow us to have messageboxes, see the files localization


# ================================
# Menu:
# __init__ => Display a welcome message
# __menu__ => Display the menu, allowing some choices
# __exit__ => Display a goodbye message
# ================================
class Menu:

    def __init__(self):
        easygui.msgbox(Strings.WELCOME, Strings.SOFTWARE_TITLE)
        

    def __menu__(self):
        title = Strings.SOFTWARE_TITLE
        message = Strings.CHOOSE_OPTION
        choices = [Strings.TXT_TO_AUDIO,Strings.WRITE_TEXT,Strings.QUIT]

        choice = easygui.choicebox(message,title,choices)

        if choice == Strings.TXT_TO_AUDIO:
            file_dir = easygui.fileopenbox(msg=None, title=None, default='*', filetypes=".txt", multiple=False)
            print file_dir
            
            # calls the function from text to audio 
        if choice == Strings.WRITE_TEXT:
            print "Write"
            # calls the function to write a text
        if choice == Strings.QUIT:
            print "Bye"
            # exits from the menu loop, must have a loop
        return self

    def __exit__(self):
        easygui.msgbox(Strings.BYE,Strings.SOFTWARE_TITLE)
        return self


###########################################
# Tests:                                  #
# All methods have passed !!!             # 
###########################################

m = Menu() 

m = m.__menu__()   

m = m.__exit__()

###########################################
