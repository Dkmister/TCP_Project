import easygui

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
        easygui.msgbox('Welcome to Text-Audio Processor','Text-Audio Processor')
        

    def __menu__(self):
        title = "Text-Audio Processor"
        message = "Choose an option"
        choices = ["Turn .txt file to audio","Write a text","Exit"]

        choice = easygui.choicebox(message,title,choices)

        if choice == "Turn .txt file to audio":
            file_dir = easygui.fileopenbox(msg=None, title=None, default='*', filetypes=".txt", multiple=False)
            print file_dir
            # calls the function from text to audio 
        if choice == "Write a text":
            print "Write"
            # calls the function to write a text
        if choice == "Exit":
            print "Bye"
            # exits from the menu loop, must have a loop
        return self

    def __exit__(self):
        easygui.msgbox('Farewell!','Text-Audio Processor')
        return self


###########################################
# Tests:                                  #
# All methods have passed !!!             # 
###########################################

m = Menu() 

m = m.__menu__()   

m = m.__exit__()

###########################################
